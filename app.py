from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    category = db.Column(db.String(10))  # OC, BC, MBC, SC, ST etc

class College(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    district = db.Column(db.String(100))
    type = db.Column(db.String(50))       # Govt / Aided / Self-Finance
    course = db.Column(db.String(100))    # B.E CSE, B.Sc Maths etc
    cutoff_mark = db.Column(db.Float)
    category = db.Column(db.String(10))
    seats = db.Column(db.Integer)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        category = request.form['category']
        
        # Check if email is already registered
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please login.')
            return redirect(url_for('register'))

        user = User(name=name, email=email, password=password, category=category)
        db.session.add(user)
        db.session.commit()
        flash('Account created! Please login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('index'))
        flash('Wrong email or password.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    results = []
    
    # Get distinct options dynamically from database
    courses = [c[0] for c in db.session.query(College.course).distinct().order_by(College.course).all()]
    districts = [d[0] for d in db.session.query(College.district).distinct().order_by(College.district).all()]
    
    # Insert 'Any' if not present
    if 'Any' not in districts:
        districts.insert(0, 'Any')

    if request.method == 'POST':
        try:
            cutoff = float(request.form['cutoff'])
        except ValueError:
            flash('Invalid cutoff value.')
            return redirect(url_for('index'))
            
        course = request.form['course']
        category = request.form['category']
        district = request.form['district']
        search_query = request.form.get('search_query', '').strip()

        query = College.query.filter(
            College.course == course,
            College.category == category,
            College.cutoff_mark <= cutoff   # student cutoff >= college cutoff
        )

        if district != 'Any':
            query = query.filter(College.district == district)
            
        if search_query:
            query = query.filter(College.name.ilike(f'%{search_query}%'))

        results = query.order_by(College.cutoff_mark.desc()).all()

    form_data = request.form if request.method == 'POST' else {}
    show_results = True if request.method == 'POST' else False

    return render_template('index.html', results=results, courses=courses, districts=districts, form_data=form_data, show_results=show_results)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5001)

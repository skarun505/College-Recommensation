from app import app, db, College

colleges = [
    {"name": "Anna University", "district": "Chennai", "type": "Government", "course": "B.E CSE", "cutoff_mark": 195.0, "category": "OC", "seats": 60},
    {"name": "Anna University", "district": "Chennai", "type": "Government", "course": "B.E CSE", "cutoff_mark": 185.0, "category": "BC", "seats": 60},
    {"name": "PSG College of Technology", "district": "Coimbatore", "type": "Aided", "course": "B.E CSE", "cutoff_mark": 188.0, "category": "OC", "seats": 60},
    {"name": "Madras Institute of Technology", "district": "Chennai", "type": "Government", "course": "B.E Mech", "cutoff_mark": 192.0, "category": "OC", "seats": 60},
    {"name": "Madras Institute of Technology", "district": "Chennai", "type": "Government", "course": "B.E Mech", "cutoff_mark": 180.0, "category": "BC", "seats": 60},
    {"name": "Coimbatore Institute of Technology", "district": "Coimbatore", "type": "Aided", "course": "B.Sc Maths", "cutoff_mark": 175.0, "category": "MBC", "seats": 40},
    {"name": "Government College of Technology", "district": "Coimbatore", "type": "Government", "course": "B.E ECE", "cutoff_mark": 190.0, "category": "OC", "seats": 60},
    {"name": "Thiagarajar College of Engineering", "district": "Madurai", "type": "Aided", "course": "B.E CSE", "cutoff_mark": 193.0, "category": "OC", "seats": 60},
    {"name": "Thiagarajar College of Engineering", "district": "Madurai", "type": "Aided", "course": "B.E CSE", "cutoff_mark": 183.0, "category": "BC", "seats": 60},
    {"name": "Madurai Diraviyam Thayumanavar Hindu College", "district": "Madurai", "type": "Aided", "course": "B.Sc Physics", "cutoff_mark": 160.0, "category": "SC", "seats": 50},
    {"name": "Government College of Engineering", "district": "Salem", "type": "Government", "course": "B.E Mech", "cutoff_mark": 170.0, "category": "MBC", "seats": 60},
    {"name": "Knowledge Institute of Technology", "district": "Salem", "type": "Self-Finance", "course": "B.E CSE", "cutoff_mark": 150.0, "category": "BC", "seats": 120},
    {"name": "National Institute of Technology", "district": "Trichy", "type": "Government", "course": "B.E CSE", "cutoff_mark": 198.0, "category": "OC", "seats": 60},
    {"name": "Saranathan College of Engineering", "district": "Trichy", "type": "Self-Finance", "course": "B.E ECE", "cutoff_mark": 165.0, "category": "BC", "seats": 60},
    {"name": "Karpagam College of Engineering", "district": "Coimbatore", "type": "Self-Finance", "course": "B.E CSE", "cutoff_mark": 155.0, "category": "SC", "seats": 120},
    {"name": "Sri Sivasubramaniya Nadar College of Engineering", "district": "Chennai", "type": "Self-Finance", "course": "B.E CSE", "cutoff_mark": 194.0, "category": "OC", "seats": 120},
    {"name": "Jeppiaar Engineering College", "district": "Chennai", "type": "Self-Finance", "course": "B.E Mech", "cutoff_mark": 140.0, "category": "MBC", "seats": 60},
    {"name": "St. Joseph's College of Engineering", "district": "Chennai", "type": "Self-Finance", "course": "B.E ECE", "cutoff_mark": 178.0, "category": "BC", "seats": 120},
    {"name": "Mepco Schlenk Engineering College", "district": "Madurai", "type": "Self-Finance", "course": "B.E CSE", "cutoff_mark": 186.0, "category": "OC", "seats": 120},
    {"name": "K.S. Rangasamy College of Technology", "district": "Salem", "type": "Self-Finance", "course": "B.E ECE", "cutoff_mark": 158.0, "category": "BC", "seats": 120},
    {"name": "MAM College of Engineering", "district": "Trichy", "type": "Self-Finance", "course": "B.E Mech", "cutoff_mark": 130.0, "category": "SC", "seats": 60},
]

with app.app_context():
    db.create_all()
    if College.query.count() == 0:
        for c in colleges:
            db.session.add(College(**c))
        db.session.commit()
        print(f"Done! Seeded {len(colleges)} records.")
    else:
        print("Database already contains data! Skipping seeding.")

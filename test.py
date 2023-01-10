from model import db, user, app


with app.app_context():
    db.create_all()
'''all=user.query.all()
p=user(user_id=101,
user_name="unni",
email="unnni@example.com",
password="pasnnnsword@example.com")
db.session.add(p)
db.session.commit()'''

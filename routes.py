from app import User, db

db.create_all()
db.session.commit()

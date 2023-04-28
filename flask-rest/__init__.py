from .app import User,db

with app.app_context():
    db.create_all()
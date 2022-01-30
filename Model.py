from main import db
class UsersNames(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    surname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
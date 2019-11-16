
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(128), nullable=False)
    name = Column(String(1000))

    @property
    def password(self):
        raise AttributeError("Password is write only")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

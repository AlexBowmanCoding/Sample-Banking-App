import email
from email.policy import default
from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Bank User class

class BankUser(db.Model):
    __tablename__ = 'bank_users' 
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    account_number = db.Column(db.Integer, unique=True, nullable=False)
    routing_number = db.Column(db.Integer, unique=True, nullable=False)
    balance = db.Column(db.Integer, nullable=False, default=0)
    

    def __init__(self, username: str, password: str, email: str, account_number: int, routing_number: int):
        self.username = username
        self.password = password
        self.email = email
        self.account_number = account_number
        self.routing_number = routing_number


    # Returns username and user id

    def serialize(self):
        return{
            'username': self.username,
            'user_id': self.user_id
        }


import imp
from flask import Flask, Blueprint, jsonify, abort, request, url_for, flash, redirect

import secrets
import hashlib

from sqlalchemy import true
from .models import BankUser, db
import random
import re   


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 




# Checks for a valid email

def check(email):   
  
    if(re.search(regex,email)):   
        return True   
    else:   
        return False   


# Hashes password so that the raw password isnt stored in the database

def scramble(password: str):
    """Hash and salt the given password"""
    salt = "QjGTeRms5Wew5ADA"
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


# Randomly generates account number
# TO DO: Create Unique account numbers

def rng_account_number():
    the_number = random.randint(10000000, 99999999) 
    return the_number


# Randomly generates routing number
# TO DO: Create Unique routing numbers

def rng_routing_number():
    the_number = random.randint(100000000, 999999999) 
    return the_number


# Creates Users using JSON input at /users 

bp = Blueprint('bank_users', __name__, url_prefix='/users')
@bp.route('', methods=['POST'])
def create():
    
    
    # Checks for username, password and email in the request.json

    if 'username' not in request.json or 'password' not in request.json or 'email' not in request.json:
        return abort(400)

    
    # Checks username and password for length requirements and checks for valid email using the check function

    if len(request.json['username']) < 3 or len(request.json['password']) < 8 or check(request.json['email']) == False:
        return abort(400)

    
    # Applies the username, password, email, account number, and routing number to the database

    u = BankUser(
        username=request.json['username'],
        password=scramble(request.json['password']),
        email=request.json['email'],
        account_number= rng_account_number(),
        routing_number= rng_routing_number()

    )
    db.session.add(u)
    db.session.commit()
    return jsonify(u.serialize())


# Returns a user via id in JSON

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = BankUser.query.get_or_404(id)
    
    return jsonify(u.serialize())


# Returns JSON of all Users

@bp.route('', methods=['GET'])
def index():
    users = BankUser.query.all()
    result = []
    for u in users:
        result.append(u.serialize())
    return jsonify(result)


# Deletes user via id 

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = BankUser.query.get_or_404(id)
    try:
        db.session.delete(u)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)


# Updates user information. 

@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    u = BankUser.query.get_or_404(id)


    # Checks for username, password, or email and aborts if not in request.json

    if 'username' not in request.json and 'password' not in request.json and 'email' not in request.json:
        return abort(400)


    # If username is in request.json it updates the user's username

    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        u.username=request.json['username']
        
    
    # If password is in request.json it updates the user's password and scrambles it

    if 'password' in request.json:
        if 'current_password' not in request.json:
            return abort(400)
        if scramble(request.json['current_password']) != u.password:
            return abort(401)
        if len(request.json['password']) < 8:
            return abort(400)
        u.password = scramble(request.json['password'])


    # If email is in request.json it updates the user's email

    if 'email' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        u.email=request.json['email']
        
    
        
    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)


# Returns Json contaning the users balance

@bp.route('/<int:id>/balance', methods=['GET'])
def get_balance(id:int):
    u = BankUser.query.get_or_404(id)
    return jsonify(u.balance)
 
        
# Adds amount to balance


@bp.route('/<int:id>/balance/add', methods=['PATCH', 'PUT'])
def deposit(id:int):
    u = BankUser.query.get_or_404(id)
    if 'amount' not in request.json  or not request.json['amount'] is not int or int(request.json['amount']) < 0:
        return(400)
    print(u.balance)
    u.balance = int(request.json['amount']) + u.balance
    db.session.commit()
    return jsonify(u.balance)


# Subtracts amount from balance
    
@bp.route('/<int:id>/balance/minus', methods=['PATCH', 'PUT'])
def withdraw(id:int):
    u = BankUser.query.get_or_404(id)
    if 'amount' not in request.json  or not request.json['amount'] is not int or int(request.json['amount']) < 0:
        return(400)
    print(u.balance)
    u.balance = u.balance - int(request.json['amount'])
    db.session.commit()
    return jsonify(u.balance)



import os
from flask import Flask
from flask_migrate import Migrate
from .models import db
from flask_sqlalchemy import SQLAlchemy

# https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/


# Creates flask app

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
    SECRET_KEY=os.environ.get("PGPASSWORD", 'Yknb4iYJNMy0WrT_NDtt1Q'),
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASEURI",'cockroachdb://aws:Yknb4iYJNMy0WrT_NDtt1Q@free-tier14.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?&options=--cluster%3Dprime-wyvern-1360'),
    #SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_ECHO=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    db.init_app(app)
    migrate = Migrate(app, db)

    from . import Bank 
    app.register_blueprint(Bank.bp)
     

    return app

app = create_app()

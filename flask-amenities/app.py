# app.py

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.local import LocalProxy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure scoped_session with sessionmaker
with app.app_context():
    db.session = scoped_session(sessionmaker(bind=db.engine, autocommit=False, autoflush=False), scopefunc=LocalProxy(lambda: current_app.app_context().push()))

# Import des routes après l'initialisation de db si nécessair
from app import routes

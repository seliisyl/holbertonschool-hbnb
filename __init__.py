# app/__init__.py

from flask import Flask
from flask_restx import Api
from app.routes import api as amenity_api

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='Amenity API', description='API for managing amenities')

    api.add_namespace(amenity_api)

    return app


from flask import request
from flask_restx import Namespace, Resource, fields
from .models import db, Amenity

api = Namespace('amenities', description='Amenities operations')

amenity_model = api.model('Amenity', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an amenity'),
    'name': fields.String(required=True, description='Amenity name'),
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime,
    })

@api.route('/')
class AmenityList(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        return Amenity.query.all()

    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created.')
    @api.response(409, 'Amenity already exists.')
    def post(self):
        data = request.json
        if Amenity.query.filter_by(name=data['name']).first():
            api.abort(409, 'Amenity already exists.')
        new_amenity = Amenity(name=data['name'])
        db.session.add(new_amenity)
        db.session.commit()
        return new_amenity, 201

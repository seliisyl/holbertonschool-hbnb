# app/routes.py

from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields
from app.models import Amenity, amenities

api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True, description='Amenity name'),
    'created_at': fields.DateTime(readonly=True),
    'updated_at': fields.DateTime(readonly=True)
})

@api.route('/')
class AmenityList(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        return amenities

    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    def post(self):
        data = request.json
        name = data.get('name')

        if not name:
            return {'message': 'Name is required'}, 400
        
        # Check for duplicate name
        if any(amenity.name == name for amenity in amenities):
            return {'message': 'Amenity with this name already exists'}, 409

        new_amenity = Amenity(id=len(amenities) + 1, name=name)
        amenities.append(new_amenity)
        return new_amenity, 201

@api.route('/<int:amenity_id>')
@api.response(404, 'Amenity not found')
class AmenityDetail(Resource):
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        amenity = next((a for a in amenities if a.id == amenity_id), None)
        if not amenity:
            api.abort(404, message="Amenity {} doesn't exist".format(amenity_id))
        return amenity

    @api.expect(amenity_model)
    @api.response(204, 'Amenity successfully updated')
    def put(self, amenity_id):
        data = request.json
        name = data.get('name')

        if not name:
            return {'message': 'Name is required'}, 400
        
        amenity = next((a for a in amenities if a.id == amenity_id), None)
        if not amenity:
            api.abort(404, message="Amenity {} doesn't exist".format(amenity_id))
        
        # Check for duplicate name
        if any(a.name == name and a.id != amenity_id for a in amenities):
            return {'message': 'Amenity with this name already exists'}, 409
        
        amenity.update(name)
        return '', 204

    @api.response(204, 'Amenity successfully deleted')
    def delete(self, amenity_id):
        global amenities
        initial_length = len(amenities)
        amenities = [a for a in amenities if a.id != amenity_id]
        if len(amenities) < initial_length:
            return '', 204
        else:
            api.abort(404, message="Amenity {} doesn't exist".format(amenity_id))


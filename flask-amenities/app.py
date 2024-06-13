from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from datetime import datetime

app = Flask(__name__)
api = Api(app, version='1.0', title='Amenities API', description='A simple Amenities API')

# In-memory database
amenities = []

# Define the Amenity model for Swagger documentation
amenity_model = api.model('Amenity', {
    'id': fields.Integer(readonly=True, description='The unique identifier of an amenity'),
    'name': fields.String(required=True, description='The name of the amenity'),
    'created_at': fields.DateTime(readonly=True, description='The date and time the amenity was created'),
    'updated_at': fields.DateTime(readonly=True, description='The date and time the amenity was last updated')
    })

# Endpoint for all amenities
@api.route('/amenities')
class AmenityList(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        return amenities

    @api.expect(amenity_model)
    @api.response(201, 'Amenity created')
    @api.response(409, 'Conflict - Amenity already exists')
    def post(self):
        """Create a new amenity"""
        data = request.json
        for amenity in amenities:
            if amenity['name'] == data['name']:
                return {'message': 'Conflict - Amenity already exists'}, 409
        new_id = len(amenities) + 1
        new_amenity = {
                'id': new_id,
                'name': data['name'],
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow()
                }
        amenities.append(new_amenity)
        return new_amenity, 201

# Endpoint for a specific amenity
@api.route('/amenities/<int:amenity_id>')
@api.response(404, 'Amenity not found')
class Amenity(Resource):
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Fetch a single amenity"""
        amenity = next((amenity for amenity in amenities if amenity['id'] == amenity_id), None)
        if amenity is None:
            return {'message': 'Amenity not found'}, 404
        return amenity

    @api.expect(amenity_model)
    @api.response(204, 'Amenity updated')
    def put(self, amenity_id):
        """Update an existing amenity"""
        data = request.json
        amenity = next((amenity for amenity in amenities if amenity['id'] == amenity_id), None)
        if amenity is None:
            return {'message': 'Amenity not found'}, 404
        amenity['name'] = data['name']
        amenity['updated_at'] = datetime.utcnow()
        return '', 204

    @api.response(204, 'Amenity deleted')
    def delete(self, amenity_id):
        """Delete an amenity"""
        global amenities
        amenities = [amenity for amenity in amenities if amenity['id'] != amenity_id]
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)


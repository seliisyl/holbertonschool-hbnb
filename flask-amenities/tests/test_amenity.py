import unittest
import json
from app import create_app
from app.models import db, Amenity

class AmenityTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.init_app(self.app)
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_amenity(self):
        response = self.client.post('/amenities', json={'name': 'Swimming Pool'})
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Swimming Pool')

    def test_get_amenity(self):
        amenity = Amenity(name='WiFi')
        with self.app.app_context():
            db.session.add(amenity)
            db.session.commit()
        response = self.client.get(f'/amenities/{amenity.id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'WiFi')

    def test_update_amenity(self):
        amenity = Amenity(name='WiFi')
        with self.app.app_context():
            db.session.add(amenity)
            db.session.commit()
        response = self.client.put(f'/amenities/{amenity.id}', json={'name': 'Free WiFi'})
        self.assertEqual(response.status_code, 204)
        with self.app.app_context():
            updated_amenity = Amenity.query.get(amenity.id)
            self.assertEqual(updated_amenity.name, 'Free WiFi')

    def test_delete_amenity(self):
        amenity = Amenity(name='WiFi')
        with self.app.app_context():
            db.session.add(amenity)
            db.session.commit()
        response = self.client.delete(f'/amenities/{amenity.id}')
        self.assertEqual(response.status_code, 204)
        with self.app.app_context():
            deleted_amenity = Amenity.query.get(amenity.id)
            self.assertIsNone(deleted_amenity)

if __name__ == '__main__':
    unittest.main()

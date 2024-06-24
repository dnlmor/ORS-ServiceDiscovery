import unittest
from app import create_app
from app.models import db_session, Service

class TestSchema(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        db_session.remove()

    def test_register_service(self):
        response = self.client.post('/graphql', json={'query': '''
            mutation {
                registerService(name: "UserService", host: "localhost", port: 5000) {
                    service {
                        id
                        name
                        host
                        port
                        registeredAt
                    }
                }
            }
        '''})
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)

    def test_get_service(self):
        # First, register a service
        self.test_register_service()
        
        response = self.client.post('/graphql', json={'query': '''
            query {
                getService(id: 1) {
                    id
                    name
                    host
                    port
                    registeredAt
                }
            }
        '''})
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)

if __name__ == '__main__':
    unittest.main()

import unittest
from app.services import ServiceDiscoveryService
from app.models import Service
from app.database import db_session

class TestServiceDiscoveryService(unittest.TestCase):
    def setUp(self):
        self.service_data = {
            'name': "UserService",
            'host': "localhost",
            'port': 5000
        }

    def test_register_service(self):
        service = ServiceDiscoveryService.register_service(**self.service_data)
        self.assertIsNotNone(service.id)
        self.assertEqual(service.name, self.service_data['name'])
        self.assertEqual(service.host, self.service_data['host'])
        self.assertEqual(service.port, self.service_data['port'])

    def test_deregister_service(self):
        service = ServiceDiscoveryService.register_service(**self.service_data)
        success = ServiceDiscoveryService.deregister_service(service.id)
        self.assertTrue(success)

    def tearDown(self):
        db_session.remove()

if __name__ == '__main__':
    unittest.main()

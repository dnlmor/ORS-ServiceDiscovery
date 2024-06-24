import unittest
from app.models import Service
from app.database import db_session

class TestServiceModel(unittest.TestCase):
    def setUp(self):
        self.service = Service(name="UserService", host="localhost", port=5000)

    def test_create_service(self):
        db_session.add(self.service)
        db_session.commit()
        self.assertIsNotNone(self.service.id)

    def tearDown(self):
        db_session.remove()

if __name__ == '__main__':
    unittest.main()

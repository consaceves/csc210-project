import unittest

from app import create_app, db


class BaseTest(unittest.TestCase):
    def create_app(self):
        return create_app()

    def setUp(self):
        self.app = self.create_app()
        self.client = self.app.test_client
        with self.app.app_context():
            from app import models
            db.drop_all()
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            from app import models
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
    unittest.main()

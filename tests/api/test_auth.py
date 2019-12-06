from tests import BaseTest
import uuid


user_data = {'id': uuid.uuid4(),
             'username': 'test',
             'password': 'testpassword',
             'name': 'test'}


class TestAuth(BaseTest):
    def test_get_home_page(self):
        res = self.client().get("/")
        self.assertEqual(res.status_code, 200)

    def test_get_create_account(self):
        res = self.client().get("/createaccount")
        self.assertEqual(res.status_code, 200)

    def test_post_create_account(self):
        res = self.client().post('/createaccount', data=user_data)
        self.assertEqual(res.status_code, 200)

    def test_unauthorized_hidden(self):
        res = self.client().get('/hidden')
        self.assertEqual(res.status_code, 401)

import os
import unittest
import jwt
from dataservice.app import app
from flask_webtest import TestApp as _TestApp


_HERE = os.path.dirname(__file__)
with open(os.path.join(_HERE, 'privkey.pem')) as f:
    _KEY = f.read()


def create_token(data):
    return jwt.encode(data, _KEY, algorithm='RS512')


_TOKEN = {'iss': 'runnerly',
          'aud': 'runnerly.io'}


class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = _TestApp(app)
        self.token = create_token(_TOKEN).decode('ascii')
        self.headers = {'Authorization': 'Bearer ' + self.token}

    def test_one(self):
        resp = self.app.get('/', headers=self.headers)
        self.assertEqual(resp.status_code, 200)

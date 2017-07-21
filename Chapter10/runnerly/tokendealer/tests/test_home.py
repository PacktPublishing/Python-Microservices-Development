import unittest
import os
from flask_webtest import TestApp as _TestApp

os.environ['TESTDIR'] = os.path.dirname(__file__)

from tokendealer.app import app         # NOQA

_SECRET = 'f0fdeb1f1584fd5431c4250b2e859457'


class TestSomething(unittest.TestCase):
    def setUp(self):
        self.app = _TestApp(app)
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def test_get_pub_key(self):
        resp = self.app.get('/.well-known/jwks.json')
        self.assertTrue('n' in resp.json[0])

    def test_roundtrip(self):
        data = [('client_id', 'strava'),
                ('client_secret', _SECRET),
                ('audience', 'audience'),
                ('grant_type', 'client_credentials')]

        resp = self.app.post('/oauth/token', params=data,
                             headers=self.headers)

        data = resp.json
        data['audience'] = 'audience'
        resp = self.app.post_json('/verify_token', params=data)
        self.assertEqual(resp.json['iss'], 'runnerly-tokendealer')

    def test_bad_creation(self):
        data = [('client_id', 'strava'),
                ('client_secret', _SECRET),
                ('audience', 'audience'),
                ('grant_type', 'wat')]

        self.app.post('/oauth/token', params=data,
                      headers=self.headers, status=400)

    def test_bad_tokens(self):
        resp = self.app.post_json('/verify_token',
                                  params={'access_token': 'd.A.D'},
                                  status=400)
        self.assertEqual(resp.json['description'], 'Invalid header padding')

        resp = self.app.post_json('/verify_token', params={},
                                  status=400)
        self.assertEqual(resp.json['description'], "'access_token'")

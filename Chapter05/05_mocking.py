import json
import unittest
from flask_extension import app, get_connector
from flask_webtest import TestApp
import requests_mock

class TestAPI(unittest.TestCase):
	def setUp(self):
		self.app = TestApp(app)
		# mocking the request calls
		session = get_connector(app)
		self.adapter = requests_mock.Adapter()
		session.mount('http://', self.adapter)
		
	def test_api(self):
		mocked_value = json.dumps({'some': 'data'})
		self.adapter.register_uri('GET', 'http://127.0.0.1:5000/api', text=mocked_value)
		res = self.app.get('/api')
		self.assertEqual(res.json['result']['some'], 'data')
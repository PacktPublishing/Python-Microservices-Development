import unittest
import json
from flask_basic import app as tested_app

class TestApp(unittest.TestCase):
	def test_help(self):
		# creating a client to interact with the app
		app = tested_app.test_client()

		# calling /api/ endpoint
		hello = app.get('/api')

		# asserting the body
		body = json.loads(str(hello.data, 'utf8'))
		self.assertEqual(body['Hello'], 'World!')

if __name__ == '__main__':
	unittest.main()
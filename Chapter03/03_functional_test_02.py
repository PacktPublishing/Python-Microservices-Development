import unittest
import json
from flask_error import app as tested_app

_404 = ('The requested URL was not found on the server. ' 'If you entered the URL manually please check your ' 'spelling and try again.')

class TestApp(unittest.TestCase):
	def setUp(self):
		# creating a client to interact with the app
		self.app = tested_app.test_client()

	def test_raise(self):
		# this won't raise a Python exception but return a 500
		hello = self.app.get('/api')
		body = json.loads(str(hello.data, 'utf8'))
		self.assertEqual(body['code'], 500)

	def test_proper_404(self):
		# calling a non existing endpoint
		hello = self.app.get('/dwdwqqwdwqd')

		# yeah it's not there
		self.assertEqual(hello.status_code, 404)

		# but we still get a nice JSON body
		body = json.loads(str(hello.data, 'utf8'))
		self.assertEqual(body['code'], 404)
		self.assertEqual(body['message'], '404: Not Found')
		self.assertEqual(body['description'], _404)

	if __name__ == '__main__':
	unittest.main()
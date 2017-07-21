import unittest
from unittest import mock
import requests
from requests.exceptions import ConnectionError
import requests_mock
import bugzilla

class TestBugzilla(unittest.TestCase):
	def test_bug_id(self):
		zilla = MyBugzilla('tarek@mozilla.com', server = 'http://yeah')
		link = zilla.bug_link(23)
		self.assertEqual(link, 'http://yeah/show_bug.cgi?id=23')

@requests_mock.mock()
def test_get_new_bugs(self, mocker):
	# mocking the requests call and send back two bugs
	bugs = [{'id': 1184528}, {'id': 1184524}]
	mocker.get(requests_mock.ANY, json={'bugs': bugs})

	zilla = MyBugzilla('tarek@mozilla.com', server = 'http://yeah')
	bugs = list(zilla.get_new_bugs())
	self.assertEqual(bugs[0]['link'], 'http://yeah/show_bug.cgi?id=1184528')

@mock.patch.object(requests, 'get', side_effect=ConnectionError('No network'))

def test_network_error(self, mocked):
	# faking a connection error in request if the web is down
	zilla = MyBugzilla('tarek@mozilla.com', server='http://yeah')
	bugs = list(zilla.get_new_bugs())
	self.assertEqual(len(bugs), 0)

if __name__ == '__main__':
	unittest.main()
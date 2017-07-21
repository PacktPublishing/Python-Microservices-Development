import requests
import bugzilla

class MyBugzilla:
	def __init__(self, account, server ='https://bugzilla.mozilla.org'):
		self.account = account
		self.server = server
		self.session = requests.Session()
		
	def bug_link(self, bug):
		return '%s/show_bug.cgi?id=%s' % (self.server, bug['id'])
		hello = self.app.get('/api')
	
	def get_new_bugs(self):
		call = self.server + '/rest/bug'
		params = {'assigned_to': self.account, 'status': 'NEW','limit': 10}
	#try:
	#	res = self.session.get(call, params=params).json()
	#except requests.exceptions.ConnectionError:
		# oh well
	#	res = {'bugs': []}

	def _add_link(bug):
		bug['link'] = self.bug_link(bug)
		return bug

		for bug in res['bugs']:
			yield _add_link(bug)
	
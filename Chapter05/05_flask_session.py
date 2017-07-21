from requests import Session

def setup_connector(app, name='default', **options):
	if not hasattr(app, 'extensions'):
		app.extensions = {}

	if 'connectors' not in app.extensions:
		app.extensions['connectors'] = {}
	session = Session()

	if 'auth' in options:
		session.auth = options['auth']
	headers = options.get('headers', {})

	if 'Content-Type' not in headers:
		headers['Content-Type'] = 'application/json'
	session.headers.update(headers)

	app.extensions['connectors'][name] = session
	return session
	
def get_connector(app, name='default'):
	return app.extensions['connectors'][name]

from gevent import monkey; monkey.patch_all()

def application(environ, start_response):
	headers = [('Content-type', 'application/json')]
	start_response('200 OK', headers)
	# ...do something with sockets here...
	return result
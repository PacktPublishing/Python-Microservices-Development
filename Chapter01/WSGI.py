import json
import jsonify, request
import time

def application(environ, start_response):
	headers = [('Content-type', 'application/json')]
	start_response('200 OK', headers)
	return bytes(json.dumps({'time': time.time()}), 'utf8')
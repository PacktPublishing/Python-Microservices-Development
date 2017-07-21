from flask import Flask, jsonify, request
import json

class XFFMiddleware(object):
	def __init__(self, app, real_ip='10.1.1.1'):
		self.app = app
		self.real_ip = real_ip

	def __call__(self, environ, start_response):
		if 'HTTP_X_FORWARDED_FOR' not in environ:
			values = '%s, 10.3.4.5, 127.0.0.1' % self.real_ip
			environ['HTTP_X_FORWARDED_FOR'] = values
		return self.app(environ, start_response)

app = Flask(__name__)
app.wsgi_app = XFFMiddleware(app.wsgi_app)

@app.route('/api')
def my_microservice():
	if "X-Forwarded-For" in request.headers:
		ips = [ip.strip() for ip in
			request.headers['X-Forwarded-For'].split(',')]
		ip = ips[0]
	else:
		ip = request.remote_addr

	return jsonify({'Hello': ip})

if __name__ == '__main__':
	app.run()
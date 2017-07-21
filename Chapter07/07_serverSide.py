from flask import Flask, request, render_template_string

app = Flask(__name__)

SECRET = 'oh no!'

_TEMPLATE = """\
Hello %s

Welcome to my API!
"""

class Extra(object):
	def __init__(self, data):
		self.data = data

@app.route('/')
def my_microservice():
	user_id = request.args.get('user_id', 'Anynomous')
	tmpl = _TEMPLATE % user_id
	return render_template_string(tmpl, extra=Extra('something'))
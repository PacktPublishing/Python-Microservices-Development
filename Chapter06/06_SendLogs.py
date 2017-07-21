import logging
import graypy
import json
from flask import Flask, jsonify, abort
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

def error_handling(error):
	if isinstance(error, HTTPException):
		result = {'code': error.code, 'description': error.description}
	else:
		description = abort.mapping[500].description
		result = {'code': 500, 'description': description}

	app.logger.exception(str(error), extra=result)
	result['message'] = str(error)
	resp = jsonify(result)
	resp.status_code = result['code']
	return resp

for code in abort.mapping:
	app.register_error_handler(code, error_handling)

@app.route('/api', methods=['GET', 'POST'])
def my_microservice():
	app.logger.info("Logged into Graylog")
	resp = jsonify({'result': 'OK', 'Hello': 'World!'})
	# this will also be logged_
	raise Exception('BAHM')
	return resp
	
if __name__ == '__main__':
	handler = graypy.GELFHandler('localhost', 12201)
	app.logger.addHandler(handler)
	app.run()
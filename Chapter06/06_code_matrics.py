import functools
import logging
import graypy
import json
import time
import random
from collections import defaultdict, deque
from flask import Flask, jsonify, g

app = Flask(__name__)

class Encoder(json.JSONEncoder):
	def default(self, obj):
		base = super(Encoder, self).default
		# specific encoder for the timed functions
		if isinstance(obj, deque):
			calls = list(obj)
			return {'num_calls': len(calls), 'min': min(calls), 'max': max(calls), 'values': calls}
		return base(obj)

def timeit(func):
	@functools.wraps(func)
	def _timeit(*args, **kw):
		start = time.time()
		try:
			return func(*args, **kw)
		finally:
			if 'timers' not in g:
				g.timers = defaultdict(functools.partial(deque, maxlen=5))
			g.timers[func.__name__].append(time.time() - start)
		return _timeit

@timeit
def fast_stuff():
	time.sleep(.001)

@timeit
def some_slow_stuff():
	time.sleep(random.randint(1, 100) / 100.)

def set_view_metrics(view_func):
	@functools.wraps(view_func)
	def _set_view_metrics(*args, **kw):
		try:
			return view_func(*args, **kw)
		finally:
			app.logger.info(json.dumps(dict(g.timers), cls=Encoder))
		return _set_view_metrics

def set_app_metrics(app):
	for endpoint, func in app.view_functions.items():
		app.view_functions[endpoint] = set_view_metrics(func)

@app.route('/api', methods=['GET', 'POST'])
def my_microservice():
	some_slow_stuff()
	for i in range(12):
		fast_stuff()
		resp = jsonify({'result': 'OK', 'Hello': 'World!'})
		fast_stuff()
	return resp

if __name__ == '__main__':
	handler = graypy.GELFHandler('localhost', 12201)

app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)
set_app_metrics(
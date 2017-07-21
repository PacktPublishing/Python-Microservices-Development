from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

@app.middleware('response')
async def convert(request, response):
	if isinstance(response, dict):
		return json(response)
	return response

@app.route("/api")
async def api(request):
	return {'some': 'data'}

app.run()
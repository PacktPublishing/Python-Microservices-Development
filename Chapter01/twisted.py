import time
from twisted.web import server, resource
from twisted.internet import reactor, endpoints

class Simple(resource.Resource):
	isLeaf = True
	def render_GET(self, request):
		request.responseHeaders.addRawHeader(b"content-type", b"application/json")
		return bytes(json.dumps({'time': time.time()}), 'utf8')

site = server.Site(Simple())
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8080)
endpoint.listen(site)
reactor.run()
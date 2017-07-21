from aiohttp import web
import time

async def handle(request):
	return web.json_response({'time': time.time()})

if __name__ == '__main__':
	app = web.Application()
	app.router.add_get('/', handle)
	web.run_app(app)
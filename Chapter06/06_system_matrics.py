import psutil
import asyncio
import signal
import graypy
import logging
import json

loop = asyncio.get_event_loop()
logger = logging.getLogger('sysmetrics')

def _exit():
	loop.stop()

def _probe():
	info = {'cpu_percent': psutil.cpu_percent(interval=None)}
	logger.info(json.dumps(info))
	loop.call_later(1., _probe)

loop.add_signal_handler(signal.SIGINT, _exit)
loop.add_signal_handler(signal.SIGTERM, _exit)
handler = graypy.GELFHandler('localhost', 12201)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
loop.call_later(1., _probe)

try:
	loop.run_forever()
finally:
	loop.close()
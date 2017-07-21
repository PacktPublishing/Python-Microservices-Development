import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests

# blocking code
def fetch(url):
	return requests.get(url).text

URLS = ['http://ziade.org', 'http://python.org', 'http://mozilla.org']

# coroutine
async def example(loop):
	executor = ThreadPoolExecutor(max_workers=3)
	tasks = []
	for url in URLS:
		tasks.append(loop.run_in_executor(executor, fetch, url))

	completed, pending = await asyncio.wait(tasks)
	for task in completed:
		print(task.result())

loop = asyncio.get_event_loop()
loop.run_until_complete(example(loop))
loop.close()
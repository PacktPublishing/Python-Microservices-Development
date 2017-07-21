import asyncio

async def compute():
	for i in range(5):
		print('compute %d' % i)
		await asyncio.sleep(.1)

async def compute2():
	for i in range(5):
		print('compute2 %d' % i)
		await asyncio.sleep(.2)

async def main():
	await asyncio.gather(compute(), compute2())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
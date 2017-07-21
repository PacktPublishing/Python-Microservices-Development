import asyncio
import aiopg

dsn = 'dbname=aiopg user=aiopg password=passwd host=127.0.0.1'

async def go():
	pool = await aiopg.create_pool(dsn)
	async with pool.acquire() as conn:
		async with conn.cursor() as cur:
			await cur.execute("SELECT 1")
			ret = []
			async for row in cur:
				ret.append(row)
			assert ret == [(1,)]
loop = asyncio.get_event_loop()
loop.run_until_complete(go())
"""An Intro to Threading in Python https://realpython.com/intro-to-python-threading/"""
"""https://realpython.com/async-io-python/"""
import asyncio
import logging

import aiohttp as aiohttp

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.text()
        logging.info(f"Fetched {url} (size={len(data)})")
        return data

async def main():
    urls = [
        # 'https://example.com',
        'https://www.pythontutorial.net/python-concurrency/python-semaphore/',
    'https://httpbin.org/get',
    'https://realpython.com',
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session,url) for url in urls]

        results = await asyncio.gather(*tasks)
    logging.info("fetched all URLS")

if __name__=="__main__":
    asyncio.run(main())

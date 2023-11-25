import asyncio
import aiohttp
import time

def func(ceva):
    print(ceva)

async def fetch(ct, url,function):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            function(f'{ct} {response.status}')
            # return f'{ct} {response.status}'

async def main():
    url = 'https://www.google.com'

    tasks = [asyncio.create_task(fetch(i,url,func)) for i in range(1000)]

    results = await asyncio.gather(*tasks)
    # for i in results:print(i)

if __name__ == '__main__':
    asyncio.run(main())





# end_time = time.perf_counter()
# execution_time = end_time - start_time
# print(f"The execution time is: {execution_time}")


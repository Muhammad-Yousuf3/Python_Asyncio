import asyncio

async def wait(n):
    await asyncio.sleep(n)
    print(f"Race Will Start In : {n} ")

async def main():
    t1=asyncio.create_task(wait(3))
    t2=asyncio.create_task(wait(2))
    t3=asyncio.create_task(wait(1))

    await t1
    await t2
    await t3

asyncio.run(main())
import asyncio
#Task 1
async def greet():
    print('Good Morning!')
    await asyncio.sleep(2)
    print('Have a Nice Day!')

asyncio.run(greet())

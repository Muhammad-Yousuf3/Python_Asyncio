# asyncio.gather() is used when we want to run multiple async functions at the same time and wait for all of them to finish together.

# 🔍 Think of gather() like:
# "Hey Python! Run all of these functions together, and when they all finish, give me the results."


import asyncio

async def Greet(name):
    await asyncio.sleep(2)
    print(f"Assalam-U-Alaikum Mr {name} , How was your day?")

async def main():
    await asyncio.gather(
        Greet('Yousuf'),
        Greet('Ali'),
        Greet('Ahmed')
    )
asyncio.run(main())


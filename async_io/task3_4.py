import asyncio

# TASK 3
async def Bake_cake():
    await asyncio.sleep(3)
    print('Making Chocolate Cake!')

async def Make_Tea():
    await asyncio.sleep(2)
    print('Making Milk Tea')

async def Main():
    t1= asyncio.create_task(Bake_cake())
    t2= asyncio.create_task(Make_Tea()) 

    await t1
    await t2   

asyncio.run(Main())


# Task 4
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
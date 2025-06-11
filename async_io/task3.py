import asyncio

# TASK 3
async def Bake_cake():
    await asyncio.sleep(3)
    print('Making Chocolate Cake!')

async def Make_Tea():
    await asyncio.sleep(2)
    print('Making Milk Tea')

async def main():
    t1= asyncio.create_task(Bake_cake())
    t2= asyncio.create_task(Make_Tea()) 

    await t1
    await t2   

asyncio.run(main())
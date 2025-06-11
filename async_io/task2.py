import asyncio

#Task 2
async def Bake_cake():
    await asyncio.sleep(3)
    print('Making Chocolate Cake!')

async def Make_Tea():
    await asyncio.sleep(2)
    print('Making Milk Tea')

async def main():
    await Bake_cake()
    await Make_Tea()    

asyncio.run(main())
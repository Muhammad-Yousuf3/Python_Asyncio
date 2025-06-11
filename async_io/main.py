import asyncio


async def task1(name):
    print(f"Create a Calculator {name}")
    await asyncio.sleep(3)
    print('Program 1 Created')

async def task2(name):
    print(f"Create a Management System {name}")
    await asyncio.sleep(3)
    print('Program 2 Created.') 

async def main():
   await task1('Yousuf') 
   print('Please Wait.....')
   await asyncio.sleep(2)
   await task2('Ali')
   
asyncio.run(main()) 

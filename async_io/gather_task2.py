import asyncio
import random
import time

async def make_pizza(pizza_number):
    print(f"Pizza {pizza_number} Started....")
    await asyncio.sleep(random.randint(1,5))
    print(f"Pizza {pizza_number} Ready!")
    return f"Pizza {pizza_number}"

async def main():
    start = time.perf_counter()

    tasks=[make_pizza(i) for i in range(1, 11)]

    results= await asyncio.gather(*tasks)
    
    end = time.perf_counter()

    print(f"Your All Pizzas Are Ready : {results}")
    print(f"Total time taken: {end - start:.1f} seconds")
asyncio.run(main())


# 💡 This code creates 10 async pizza-making tasks using a list comprehension.
# Each pizza takes random time (1 to 5 seconds).
# asyncio.gather(*tasks) runs them all in parallel.
# It collects their return values into a list.
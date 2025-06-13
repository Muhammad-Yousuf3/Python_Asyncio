import time
import asyncio

async def make_cheese_pizza():
    print("Cheese Pizza Started....")
    await asyncio.sleep(3)
    print("Cheese Pizza Ready!")

    return "Cheese Pizza"

async def make_veggie_pizza():
    print("Veggie Pizza Started....")
    await asyncio.sleep(5)
    print("Veggie Pizza Ready!")

    return "Veggie Pizza"

async def make_pepperoni_pizza():
    print("Pepperoni Pizza Started....")
    await asyncio.sleep(2)
    print("Pepperoni Pizza Ready!")

    return "Pepperoni Pizza"

async def main():
    start = time.perf_counter()

    pizzas= await asyncio.gather(
        make_cheese_pizza(),
        make_veggie_pizza(),
        make_pepperoni_pizza()
        )
    
    end = time.perf_counter()

    print(f"Your All Pizzas Are Ready : {pizzas}")
    print(f"Total time taken: {end - start:.1f} seconds")
asyncio.run(main())


# 💡 This code runs 3 pizza-making functions concurrently using asyncio.gather().
# Each function returns the name of the pizza when it's ready.
# The final output prints the list of all ready pizzas and the total time taken.
# Remember: gather() collects return values from all async functions in a list.
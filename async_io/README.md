# 🌟 1. What is asyncio?
asyncio is a Python library that lets you write concurrent code using the async and await syntax. It helps you run multiple tasks at the same time without using threads or processes.

# 🚀 2. Basic Concepts
Here's a list of the core concepts you need to know:

## Concept	Explanation
`async def`  ===> Defines an asynchronous function.

`await`	===> Pauses the function until the awaited task finishes.

`asyncio.run()`  ===> Starts the event loop and runs an async function.

`asyncio.sleep()`	===> Like time.sleep(), but non-blocking.

`asyncio.create_task()`	===> Schedules a coroutine to run in the background.
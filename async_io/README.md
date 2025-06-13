# 🌀 Python asyncio Summary – by Muhammad Yousuf

A concise guide to the core concepts of Python’s asyncio library, focusing on non-blocking, concurrent execution.

---
## 🌟 1. What is asyncio?
asyncio is a Python library that lets you write concurrent code using the async and await syntax. It helps you run multiple tasks at the same time without using threads or processes.

---
## ✅ Concepts Covered

### 1. async def
Defines a coroutine, which allows non-blocking, asynchronous execution.

### 2. await
Pauses a coroutine until the awaited task is complete; used only inside async functions.

### 3. asyncio.run()
Starts the main async program and manages the event loop; used only once per script.

### 4. asyncio.sleep()
Suspends the current coroutine for a given number of seconds without blocking the program.

### 5. asyncio.create_task()
Schedules an async function to run independently; allows multiple coroutines to start in parallel.

### 6. asyncio.gather()
Runs multiple async functions at the same time and waits for all to complete; returns their results as a list.

### 7. Returning Values from Async Functions
Async functions can return values, which can be collected using gather() for further processing.

### 8. Dynamic Task Creation
Tasks can be created in a loop and executed together using gather(), useful for bulk processing like file downloads or API calls.

---

### ✍️ Author: Muhammad Yousuf  
Python Student | GIAIC  
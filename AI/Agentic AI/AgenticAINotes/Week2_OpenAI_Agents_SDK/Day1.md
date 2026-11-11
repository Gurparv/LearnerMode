## 'asyncio' 

All the Agents Frameworks use ==asynchronous python== so below are my study notes of it.

- Asyncio provides a lightweight alternative to threading or multi-processing.It is different than 'Threads',  and 'Multiprocessing'. ==It is a inbuilt python package along with some python keywords/language contructs (like await , async.==
- Functions defined with ==async def== are called ==coroutines== - they're special functions that can be paused and resumed.
- Calling a coroutine doesnt execute it immediately - it returns a coroutine object.
- To actually run a coroutine, you must ==await== it , which schedules it for execution within an ==event loop==
- While a coroutine is waiting (eg for I/O), the ==event loop== can run other coroutines

```python
# Example1
async def do_something() -> str:
	# do work
	return "done!"

result = await do_something() 
```

```python
# Example2

async def do_something() -> str:
	# do work
	return "done!"
	
# running the function returns a couroutine
my_coroutine = do_something()

# awaiting the coroutine returns a result
result = await my_coroutine
```

```python

results = await asyncio.gather(
	do_work(),
	do_otherwork(),
	do_someotherwork()
)

```

---

## Introducing OpenAI Agents SDK

- Lightweight and Flexible
- Stays out of the way.
- Makes common activities easy
- Instructor's Favourite

## Terminology

- ==Agents== represent LLMs
- ==Handoffs== represent interactions
- ==Guardrails== represent controls(checks,validations you implement)


## Three Steps

1. Create an instance of ==Agent==
2. Use ==with trace()== to track the agent.
3. Call ==runner.run()== to run the agent. // this is an async function that is a coroutine.


## Platform to check 'Traces' output

https://platform.openai.com/logs?api=traces

## Vibe Coding

1. ==Good vibes== : Prompt well - ask for short answers and latest API's for today's date
2. ==Vibe but verify== : ask 2 LLMs the same question
3. ==Step up the vibe== : ask to break down your request into independently testable steps.
4. ==Vibe and validate== : ask an LLM then get another LLM to check.
5. ==Vibe with variety== - ask for 3 solution to the same problem, pick the best.




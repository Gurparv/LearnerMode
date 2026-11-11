from dotenv import load_dotenv
from agents import Agent,Runner, trace
import asyncio

load_dotenv(override = True)
agent = Agent(name="Jokestar", instructions="You are a joke teller", model = "gpt-4o-mini")

print(agent)

result = Runner.run(agent, "Tell a joke about Autonomous AI Agents")
print(result) # Returns coroutine.

##############################

async def get_result():
    result2 = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
    print(result2) # Retunrs answer
    print(result2.final_output)

asyncio.run(get_result())

##############################
# Using a trace for recording on the site -> https://platform.openai.com/logs?api=traces
with trace("Telling a joke"):
    asyncio.run(get_result())


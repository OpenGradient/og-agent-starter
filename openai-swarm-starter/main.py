import os

from agent import og_agent
from swarm import Swarm
from opengradient.llm import openai_adapter

# User input
USER_PROMPT = "hello, what is the price of ETH?"

if not os.environ.get("PRIVATE_KEY"):
    raise Exception("Please set PRIVATE_KEY to your OpenGradient private key")

swarm_client = Swarm(client=openai_adapter(os.environ.get("PRIVATE_KEY")))

response = swarm_client.run(
    agent=og_agent,
    debug=False, # Set to true for debugging agent
    # Instruction for the agent on what to do
    messages=[{
        "role": "user", 
        "content": USER_PROMPT,
    }],
)

# Print result
print(response.messages[-1]["content"])
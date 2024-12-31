import os

from swarm import Swarm
from opengradient.llm import openai_adapter

from agent import create_agent

# User input
USER_PROMPT = "hello, what is the price of ETH?"

if not os.environ.get("PRIVATE_KEY"):
    raise Exception("Please set PRIVATE_KEY to your OpenGradient private key")

swarm_client = Swarm(client=openai_adapter(os.environ.get("PRIVATE_KEY")))
agent = create_agent()

response = swarm_client.run(
    agent=agent,
    # Instruction for the agent on what to do
    messages=[{
        "role": "user", 
        "content": USER_PROMPT,
    }],
    debug=False, # Set to true for debugging agent
)

# Print result
print(response.messages[-1]["content"])
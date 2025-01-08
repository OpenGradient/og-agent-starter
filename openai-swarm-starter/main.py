import os

from dotenv import load_dotenv
from swarm import Swarm
from opengradient.llm import openai_adapter

from agent import create_agent

# Load environment variables from .env file
load_dotenv("../.env.sh")

# User input
USER_PROMPT = "post something funny"

private_key = os.environ.get('PRIVATE_KEY')
if not private_key:
    raise Exception("Must set PRIVATE_KEY env var")

swarm_client = Swarm(client=openai_adapter(private_key))
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
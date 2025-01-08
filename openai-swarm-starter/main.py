import os
import sys

from dotenv import load_dotenv
from swarm import Swarm
from opengradient.llm import openai_adapter

from agent import create_agent

# Load environment variables from .env file
load_dotenv("../.env.sh")

# Check argument
if len(sys.argv) != 2:
    print("Usage: python main.py 'your prompt here'")
    sys.exit(1)
user_prompt = sys.argv[1]

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
        "content": user_prompt,
    }],
    debug=False, # Set to true for debugging agent
)

# Print result
print(response.messages[-1]["content"])
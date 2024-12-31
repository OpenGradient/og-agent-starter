import os
from og_adapter import OGClient
from agent import memecoin_agent
from swarm import Swarm

if not os.environ.get("PRIVATE_KEY"):
    raise Exception("Please set PRIVATE_KEY to your OpenGradient private key")

client = Swarm(client=OGClient(os.environ.get("PRIVATE_KEY")))

# change this prompt to make the agent do different things
USER_PROMPT = "Create a pepe frog token, and post an announcement about it"

response = client.run(
    agent=memecoin_agent,
    debug=False,
    # Instruction for the agent on what to do
    messages=[{
        "role": "user", 
        "content": USER_PROMPT,
    }],
)

print(response.messages[-1]["content"])
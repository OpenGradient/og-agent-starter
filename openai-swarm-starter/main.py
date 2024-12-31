import os
from agent import og_agent
from swarm import Swarm
from opengradient.llm import openai_adapter

if not os.environ.get("PRIVATE_KEY"):
    raise Exception("Please set PRIVATE_KEY to your OpenGradient private key")

client = Swarm(client=openai_adapter(os.environ.get("PRIVATE_KEY")))

# change this prompt to make the agent do different things
USER_PROMPT = "Create a pepe frog token, and post an announcement about it"

response = client.run(
    agent=og_agent,
    debug=False,
    # Instruction for the agent on what to do
    messages=[{
        "role": "user", 
        "content": USER_PROMPT,
    }],
)

print(response.messages[-1]["content"])
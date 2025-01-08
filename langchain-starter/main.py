import os

from dotenv import load_dotenv
from agent import create_agent_executor
import opengradient as og

# Load environment variables from .env file
load_dotenv()

og.init(private_key=os.environ.get('PRIVATE_KEY'), email=None, password=None)

# User input
USER_MESSAGE = "What is the price forecast for SUI?"

agent = create_agent_executor()

# Execute agent
events = agent.stream(
    {"messages": [("user", USER_MESSAGE)]},
    stream_mode="values",
    debug=True # Set to True for debugging
)

# Print reasoning and result
for event in events:
    event["messages"][-1].pretty_print()

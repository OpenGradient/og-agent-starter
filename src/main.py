from twitter_langchain import (
    TwitterApiWrapper,
    TwitterToolkit
)

import os
import uuid

from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from opengradient.llm import OpenGradientChatModel

PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
if not PRIVATE_KEY:
    raise Exception("Must set PRIVATE_KEY env var")

# Initialize TwitterApiwrapper
twitter_api_wrapper = TwitterApiWrapper()

# Create TwitterToolkit from the api wrapper
twitter_toolkit = TwitterToolkit.from_twitter_api_wrapper(twitter_api_wrapper)
tools = twitter_toolkit.get_tools()

llm = OpenGradientChatModel(
    private_key=PRIVATE_KEY,
    model_cid='NousResearch/Hermes-3-Llama-3.1-70B')

# Create agent
agent_executor = create_react_agent(llm, tools)

# Example - post tweet
events = agent_executor.stream(
    {"messages": [("user", "You are degen warren buffett who turned into a crypto bro, mimic his style. Tweet something funny about dogecoin")]},
    stream_mode="values"
)

for event in events:
    event["messages"][-1].pretty_print()
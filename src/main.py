from twitter_langchain import (
    TwitterApiWrapper,
    TwitterToolkit
)

import os

from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from opengradient.llm import OpenGradientChatModel

from prompts import KAKEGURUI_PROMPT

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
    model_cid='meta-llama/Llama-3.1-70B-Instruct')

# Create agent
agent_executor = create_react_agent(llm, tools)

# Example - post tweet
events = agent_executor.stream(
    {"messages": [
        ("system", KAKEGURUI_PROMPT),
        ("user", "hello")]},
    stream_mode="values",
    debug=False
)

for event in events:
    event["messages"][-1].pretty_print()
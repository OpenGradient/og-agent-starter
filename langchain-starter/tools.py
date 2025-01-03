from typing import List

from twitter_langchain import (
    TwitterApiWrapper,
    TwitterToolkit
)
from langchain_core.tools import BaseTool

from mltool import create_og_model_tool


# Define the tools the agent can use
def create_agent_toolkit() -> List[BaseTool]:
    twitter_api_wrapper = TwitterApiWrapper()
    twitter_toolkit = TwitterToolkit.from_twitter_api_wrapper(twitter_api_wrapper)
    tools = twitter_toolkit.get_tools()

    return tools
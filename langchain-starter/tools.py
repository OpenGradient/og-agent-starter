from typing import List

from twitter_langchain import (
    TwitterApiWrapper,
    TwitterToolkit
)
from langchain_core.tools import BaseTool
from pydantic import BaseModel
from opengradient.mltool import create_og_model_tool, ToolType


# Define the tools the agent can use
def create_agent_toolkit() -> List[BaseTool]:
    twitter_api_wrapper = TwitterApiWrapper()
    twitter_toolkit = TwitterToolkit.from_twitter_api_wrapper(twitter_api_wrapper)
    tools = twitter_toolkit.get_tools()

    tools = []

    # Add Spot Forecast model
    tools.append(create_og_model_tool(
        tool_type=ToolType.LANGCHAIN,
        model_cid="QmY1RjD3s4XPbSeKi5TqMwbxegumenZ49t2q7TrK7Xdga4",
        tool_name="SuiSpotForecast",
        input_getter=lambda: {"open_high_low_close": [
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4]
        ]},
        output_formatter=lambda out: f"The predicted price change is: {out['destandardized_prediction'][0] * 100}%",
        tool_description="Runs an ML model to forecast the price of SUI 30 minutes from now. Requires no input."
    ))

    return tools

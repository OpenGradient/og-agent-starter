import os

from langgraph.prebuilt import create_react_agent

from opengradient.llm import langchain_adapter
from opengradient import LLM

from prompts import AGENT_SYSTEM_PROMPT
from tools import create_agent_toolkit

def create_agent_executor():
    private_key = os.environ.get('PRIVATE_KEY')
    if not private_key:
        raise Exception("Must set PRIVATE_KEY env var")

    # Initialize LLM
    llm = langchain_adapter(
        private_key=private_key,
        model_cid=LLM.QWEN_2_5_72B_INSTRUCT)

    # Create agent
    agent_executor = create_react_agent(
        model=llm, 
        tools=create_agent_toolkit(),
        messages_modifier=AGENT_SYSTEM_PROMPT)

    return agent_executor
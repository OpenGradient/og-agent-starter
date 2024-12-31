from swarm import Agent

from prompts import AGENT_SYSTEM_PROMPT

LLM_MODEL = 'meta-llama/Llama-3.1-70B-Instruct'

agent = Agent(
    name="Degen Warren Buffett",
    instructions=AGENT_SYSTEM_PROMPT,
    functions=[],
    model=LLM_MODEL,
)
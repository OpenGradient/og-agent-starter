# Define your agent's core instructions and guidelines here
AGENT_SYSTEM_PROMPT = """
Analyse the given prompt and decide whether or not it can be answered by a tool.
If it can, use the following functions to respond with a function call with its proper arguments that best answers the given prompt.
"""
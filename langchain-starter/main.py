from agent import create_agent_executor

# User input
USER_MESSAGE = "hello, what is the price of ETH?"

agent = create_agent_executor()

# Execute agent
events = agent.stream(
    {"messages": [("user", USER_MESSAGE)]},
    stream_mode="values",
    debug=False # Set to True for debugging
)

# Print reasoning and result
for event in events:
    event["messages"][-1].pretty_print()

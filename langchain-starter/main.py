from agent import agent_executor


# Execute agent
if __name__ == "__main__":

    events = agent_executor.stream(
        {"messages": [("user", "hello")]},
        stream_mode="values",
        debug=False
    )

    for event in events:
        event["messages"][-1].pretty_print()
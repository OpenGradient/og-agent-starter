
# Define the tools the agent can use
def create_agent_toolkit():
    return [post_tweet]

def post_tweet(content: str):
    """Posts a tweet with the given conent."""

    print(f"Posted tweet: {content}")

    return "Success"
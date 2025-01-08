
# Define the tools the agent can use
def create_agent_toolkit():
    return [post_tweet, swap_token]

def post_tweet(content: str):
    """Sends a tweet with the given text"""

    print(f"Posted tweet: {content}")

    return "Success"

def swap_token(token_a: str, token_b: str, token_a_amount: float):
    """Swaps token A to token B with the specified amount"""

    print(f"Swapped {token_a_amount} {token_a} to {token_b}")

    return "Successfully swapped"
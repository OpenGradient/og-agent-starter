# OpenGradient + LangChain Agent

Combines OpenGradient's verifiable inference and advanced ML tools with LangChain.

## Structure

- The agent's tools are defined in `tools.py`
- The agent's prompts and instructions are in `prompts.py`
- The agent itself is defined (using the tools and prompts) in `agent.py`
- The main function for executing the agent is in `main.py`

## Setup

- Dependencies are defined in `requirements.txt`, run `pip install -r requirements.txt` to install all dependencies. We recommend using virtualenv.
- You'll need an OpenGradient token in order to run inferences. You can use the `opengradient` CLI to create it, read more on our [official docs](https://docs.opengradient.ai/developers/sdk/#credentials-setup).

## Execute

To run the agent, simply run `python main.py`

Next, you can add new tools, prompts, etc to customize the agent's behaviour.

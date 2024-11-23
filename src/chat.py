import os

from langchain_core.messages import HumanMessage, SystemMessage
from opengradient.llm import OpenGradientChatModel

from prompts import KAKEGURUI_PROMPT
import opengradient as og

PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
if not PRIVATE_KEY:
    raise Exception("Must set PRIVATE_KEY env var")

og.init(private_key=PRIVATE_KEY, email=None, password=None)

messages = [
    {'role':'system', 'content': KAKEGURUI_PROMPT},
    {'role': 'user', 'content':  "are you a capitalist?"}
]

answer = og.llm_chat(
    model_cid='meta-llama/Llama-3.1-70B-Instruct',
    messages=messages,
    max_tokens=300,
    temperature=0.4
)

print(answer)

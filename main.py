import os

from dotenv import load_dotenv
from openrouter import OpenRouter

load_dotenv()

MODEL = "openrouter/free"
PROMPT = "Hi, what's your name?"

with OpenRouter(api_key=os.environ["OPENROUTER_API_KEY"]) as open_router:
    res = open_router.chat.send(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT}],
        stream=False,
    )

print(res.choices[0].message.content)

import os
from rich import print
from openai import OpenAI


base_url = "https://openrouter.ai/api/v1"
api_key = os.environ.get("OPENROUTER_API_KEY", "")
model_id="google/gemini-2.5-flash-preview"

client = OpenAI(
    base_url=base_url,
    api_key=api_key
)

messages = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': '你是谁？'}
    ]

completion = client.chat.completions.create(
        model=model_id,
        messages=messages,
        stream=False
    )
print(completion.choices[0].message)

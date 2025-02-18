from rich import print
from provider import client, model_id


messages = [
    {
        "role": "user",
        "content": "Please write quick sort code"
    },
    {
        "role": "assistant",
        "content": "```python\n",
        "partial": True
    }
]

completion = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stop=["````"]
)
print(completion.choices[0].message.content)

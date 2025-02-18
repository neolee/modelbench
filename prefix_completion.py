from rich import print
from provider import client_beta, model_id


messages = [
    {
        "role": "user",
        "content": "Please write quick sort code"
    },
    {
        "role": "assistant",
        "content": "```python\n",
        "prefix": True,
        "partial": True
    }
]

completion = client_beta.chat.completions.create(
    model=model_id,
    messages=messages,
    stop=["```"]
)
print(completion.choices[0].message.content)

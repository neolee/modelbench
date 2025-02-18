from rich import print
from provider import chat_completion


messages = [
    {
        "role": "user",
        "content": "请对“春天来了，大地”这句话进行续写，来表达春天的美好和作者的喜悦之情"
    },
    {
        "role": "assistant",
        "content": "春天来了，大地",
        "partial": True
    }
]

completion = chat_completion(messages)
print(completion.choices[0].message.content)

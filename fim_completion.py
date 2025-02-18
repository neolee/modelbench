from rich import print
from provider import client_beta, model_id


# only work on DeepSeek beta server
try:
    assert model_id == "deepseek-chat", "This test is for DeepSeek beta server only"
except AssertionError as msg:
    print(msg)
    exit()

messages = [
    {"role": "user", "content": "Please write quick sort code"},
    {"role": "assistant", "content": "```python\n", "prefix": True}
]

response = client_beta.completions.create(
    model=model_id,
    prompt="def fib(a):",
    suffix="    return fib(a-1) + fib(a-2)",
    max_tokens=128
)
print(response.choices[0].text)

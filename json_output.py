import json
from rich import print
from provider import client, model_id


system_prompt = """
The user will provide some exam text. Please parse the "question" and "answer" and output them in JSON format.

EXAMPLE INPUT:
Which is the highest mountain in the world? Mount Everest.

EXAMPLE JSON OUTPUT:
{
    "question": "Which is the highest mountain in the world?",
    "answer": "Mount Everest"
}
"""

user_prompt = "Which is the longest river in the world? The Nile River."

messages = [{"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}]

response = client.chat.completions.create(
    model=model_id,
    messages=messages, # type: ignore
    response_format={
        'type': 'json_object'
    }
)

s = response.choices[0].message.content
print(s)
if s: print(json.loads(s))

from provider import system_message, chat_completion


welcome_message = "Introduce yourself to someone opening this program for the first time. Be concise."

history = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": welcome_message},
]

while True:
    new_message = {"role": "assistant", "content": ""}
    completion = chat_completion(history, stream=True)
    for chunk in completion:
        s = chunk.choices[0].delta.content # type: ignore
        print(s or "", end="", flush=True)
        if s: new_message["content"] += s
    print()

    history.append(new_message)

    print()

    q = input("> ")
    if q in [':q', ':x', ':quit', ':exit', 'bye']: break
    history.append({"role": "user", "content": q})

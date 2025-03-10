from runner import Runner
from mal.openai.model import append_message, chat_completion_chunk_content


class ChatRunner(Runner):
    description = "Basic Chat"

    def run(self):
        messages = [
            {
                "role": "system",
                "content": "Introduce yourself to someone opening this program for the first time. Be concise."
            },
            {
                "role": "user",
                "content": "You are a helpful assistant."
            },
        ]

        while True:
            new_message = ""

            completion = self.create_chat_completion(messages, stream=True)
            for chunk in completion:
                s = chat_completion_chunk_content(chunk)
                print(s or "", end="", flush=True)
                if s: new_message += s

            print()
            append_message(messages, "assistant", new_message)
            print()

            q = input("> ")
            if q in [':q', ':x', ':quit', ':exit', 'bye']: break
            append_message(messages, "user", q)


if __name__ == "__main__":
    r = ChatRunner()
    r.run()

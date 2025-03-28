from rich import print

from runner import Runner
from mal.openai.model import chat_completion_content


class PrefixCompletionRunner(Runner):
    description = "Prefix Completion"

    def run(self):
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

        completion = self.create_chat_completion(
            messages,
            is_beta=True,
            stop=["```"]
        )
        print(chat_completion_content(completion))


if __name__ == "__main__":
    r = PrefixCompletionRunner()
    r.run()

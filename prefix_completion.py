from rich import print
from runner import Runner


class PrefixCompletionRunner(Runner):
    desc = "Prefix Completion"

    def run(self):
        self.messages = [
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

        completion = self.client_beta.chat.completions.create(
            model=self.model_id,
            messages=self.messages,
            stop=["```"]
        )
        print(completion.choices[0].message.content)


if __name__ == "__main__":
    r = PrefixCompletionRunner()
    r.run()

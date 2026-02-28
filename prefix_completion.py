from rich import print

from runner import Runner


class PrefixCompletionRunner(Runner):
    name = "Prefix Completion"

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

        result = self.model.request_model_contents(
            messages,
            stream=False,
            is_beta=True,
            stop=["```"]
        )
        print(result["content"])


if __name__ == "__main__":
    r = PrefixCompletionRunner()
    r.run()

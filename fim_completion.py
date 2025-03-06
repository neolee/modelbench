from rich import print
from runner import Runner


class FIMCompletion(Runner):
    desc = "FIM Completion"

    def run(self):
        # for now only work on deepseek beta server
        self.messages = [
            {"role": "user", "content": "Please write quick sort code"},
            {"role": "assistant", "content": "```python\n", "prefix": True}
        ]

        completion = self.client_beta.completions.create(
            model=self.model_id,
            prompt="def fib(a):",
            suffix="    return fib(a-1) + fib(a-2)",
            max_tokens=128
        )
        print(completion.choices[0].text)


if __name__ == "__main__":
    r = FIMCompletion()
    r.run()

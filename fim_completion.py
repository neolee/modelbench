from rich import print
from runner import Runner


class FIMCompletion(Runner):
    desc = "FIM Completion"

    def run(self):
        # for now only work on DeepSeek beta server
        try:
            assert self.model_id == "deepseek-chat", "This test is for DeepSeek beta server only"
        except AssertionError as msg:
            print(msg)
            exit()

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

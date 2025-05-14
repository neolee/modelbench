from rich import print

from runner import Runner
from mal.openai.model import completion_text
import mal.openai.model as m


class FIMCompletion(Runner):
    description = "FIM Completion"

    def run(self):
        # for now only work on deepseek beta server
        completion = self.create_completion(
            is_beta=True,
            prompt="def fib(a):",
            suffix="    return fib(a-1) + fib(a-2)",
            max_tokens=128
        )
        print(completion_text(completion))


if __name__ == "__main__":
    r = FIMCompletion(m.deepseek)
    r.run()

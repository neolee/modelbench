from rich import print
from runner import Runner


class ReasonerRunner(Runner):
    def run(self):
        self.messages = []

        def reasoning(q: str):
            self.messages.append({"role": "user", "content": q})
            completion = self.reasoning_completion(stream=True)

            reasoning_content = ""
            content = ""

            for chunk in completion:
                r = chunk.choices[0].delta.reasoning_content # type: ignore
                s = chunk.choices[0].delta.content # type: ignore
                if r:
                    print(r, end="", flush=True)
                    reasoning_content += r
                elif s:
                    print(s, end="", flush=True)
                    content += s

                self.messages.append({"role": "assistant", "content": content})

        # round 1
        q1 = "9.11 and 9.8, which is greater?"
        reasoning(q1)

        print("\n")

        # round 2
        q2 = "How many Rs are there in the word 'strawberry'?"
        reasoning(q2)


if __name__ == "__main__":
    r = ReasonerRunner()
    r.run()

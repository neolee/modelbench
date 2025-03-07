from rich import print
from runner import Runner


class ReasoningRunner(Runner):
    description = "Reasoning"

    def run(self):
        self.clear_messages()

        def reasoning(q: str):
            self.add_message("user", q)
            completion = self.reasoning_completion(stream=True)

            reasoning_content = ""
            content = ""
            is_answering = False

            print("\n" + "<thinking>")
            for chunk in completion:
                r = chunk.choices[0].delta.reasoning_content # type: ignore
                s = chunk.choices[0].delta.content # type: ignore
                if r:
                    print(r, end="", flush=True)
                    reasoning_content += r
                elif s:
                    if not is_answering:
                        print("\n" + "</thinking>" + "\n")
                        is_answering = True
                    print(s, end="", flush=True)
                    content += s

            self.add_message("assistant", content)
            print()

        # round 1
        q1 = "9.11 and 9.8, which is greater?"
        reasoning(q1)

        # round 2
        q2 = "How many Rs are there in the word 'strawberry'?"
        reasoning(q2)


if __name__ == "__main__":
    r = ReasoningRunner()
    r.run()

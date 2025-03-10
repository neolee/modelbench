from rich import print

from runner import Runner
from mal.openai.model import append_message, chat_completion_chunk_content, chat_completion_chunk_reasoning_content


class ReasoningRunner(Runner):
    description = "Reasoning"

    def run(self):
        messages = []

        def reasoning(q: str):
            append_message(messages, "user", q)
            completion = self.create_chat_completion(
                messages,
                model_type="reasoner",
                stream=True
            )

            reasoning_content = ""
            content = ""
            is_answering = False

            print("\n" + "<thinking>")
            for chunk in completion:
                r = chat_completion_chunk_reasoning_content(chunk)
                s = chat_completion_chunk_content(chunk)
                if r:
                    print(r, end="", flush=True)
                    reasoning_content += r
                elif s:
                    if not is_answering:
                        print("\n" + "</thinking>" + "\n")
                        is_answering = True
                    print(s, end="", flush=True)
                    content += s

            append_message(messages, "assistant", content)
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

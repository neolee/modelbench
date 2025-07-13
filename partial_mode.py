from rich import print

from mal.openai.client import chat_completion_content

from runner import Runner


class PartialModeRunner(Runner):
    description = "Partial Mode"

    def run(self):
        messages = [
            {
                "role": "user",
                "content": "请对“春天来了，大地”这句话进行续写，来表达春天的美好和作者的喜悦之情"
            },
            {
                "role": "assistant",
                "content": "春天来了，大地",
                "prefix": True,
                "partial": True
            }
        ]

        completion = self.create_chat_completion(
            messages,
            is_beta=True
        )
        print(chat_completion_content(completion))


if __name__ == "__main__":
    r = PartialModeRunner()
    r.run()

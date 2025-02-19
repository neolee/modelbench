from rich import print
from runner import Runner


class PartialModeRunner(Runner):
    def run(self):
        self.messages = [
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

        completion = self.chat_completion()
        print(completion.choices[0].message.content) # type: ignore


if __name__ == "__main__":
    r = PartialModeRunner()
    r.run()

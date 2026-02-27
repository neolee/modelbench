from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown

from util.rich import prettier_code_blocks

from runner import Runner


class ChatRunner(Runner):
    name = "Basic Chat"

    def run(self):
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Introduce yourself to someone opening this program for the first time. Be concise."
            }
        ]

        prettier_code_blocks()
        console = Console()
        while True:
            reasoning_content = ""
            content = ""
            is_thinking = False
            is_answering = False

            # Use clean completion to automatically separate reasoning and content
            completion = self.model.create_chat_completion_clean(messages, stream=True)
            # TODO the `vertical_overflow='visible'` param can provider continuous down scrolling
            #      but make a mess on up scrolling
            with Live('', console=console) as live:
                for event in completion:
                    if event["type"] == "reasoning":
                        if not is_thinking:
                            reasoning_content += "# Think\n"
                            is_thinking = True
                        reasoning_content += event["delta"]
                        live.update(Markdown(reasoning_content))
                    elif event["type"] == "content":
                        if not is_answering:
                            if is_thinking:
                                reasoning_content += "\n# Answer\n"
                                is_thinking = False
                            is_answering = True
                        content += event["delta"]
                        live.update(Markdown(reasoning_content + content))

                console.print()

            self.model.append_message(messages, "assistant", content)
            console.print()

            q = console.input("[bold blue]>[/] ")
            if q in [':q', ':x', ':quit', ':exit', 'bye']: break
            self.model.append_message(messages, "user", q)


if __name__ == "__main__":
    r = ChatRunner()
    r.run()

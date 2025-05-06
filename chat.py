from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown

from runner import Runner
from mal.openai.model import append_message, chat_completion_chunk_content
from util.rich import prettier_code_blocks


class ChatRunner(Runner):
    description = "Basic Chat"

    def run(self):
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Introduce yourself to someone opening this program for the first time. Be concise."
            },
        ]

        prettier_code_blocks()
        console = Console()
        while True:
            message = ""

            completion = self.create_chat_completion(messages, stream=True)
            # TODO the `vertical_overflow='visible'` param can provider continuous down scrolling
            #      but make a mess on up scrolling
            with Live('', console=console) as live:
                for chunk in completion:
                    s = chat_completion_chunk_content(chunk)
                    if s:
                        message += s
                        live.update(Markdown(message))

                console.print()

            append_message(messages, "assistant", message)
            console.print()

            q = console.input("[bold blue]>[/] ")
            if q in [':q', ':x', ':quit', ':exit', 'bye']: break
            append_message(messages, "user", q)


if __name__ == "__main__":
    r = ChatRunner()
    r.run()

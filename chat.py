import re
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

            completion = self.create_chat_completion(messages, stream=True)
            # TODO the `vertical_overflow='visible'` param can provider continuous down scrolling
            #      but make a mess on up scrolling
            with Live('', console=console) as live:
                for chunk in completion:
                    r = self.model.chat_completion_chunk_reasoning_content(chunk)
                    s = self.model.chat_completion_chunk_content(chunk)
                    if r:
                        if not is_thinking:
                            reasoning_content += "# Think\n"
                            is_thinking = True
                        reasoning_content += r
                        live.update(Markdown(reasoning_content))
                    elif s:
                        if not is_answering:
                            if is_thinking:
                                reasoning_content += "\n# Answer\n"
                                is_thinking = False
                            is_answering = True
                        s = re.sub(r"<think>", "# Think\n", s)
                        s = re.sub(r"</think>", "\n# Answer\n", s)
                        content += s
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

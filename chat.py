from runner import Runner


class ChatRunner(Runner):
    desc = "Basic Chat"

    def run(self):
        while True:
            new_message = ""
            completion = self.chat_completion(stream=True)
            for chunk in completion:
                s = chunk.choices[0].delta.content # type: ignore
                print(s or "", end="", flush=True)
                if s: new_message += s

            print()
            self.add_message("assistant", new_message)
            print()

            q = input("> ")
            if q in [':q', ':x', ':quit', ':exit', 'bye']: break
            self.add_message("user", q)


if __name__ == "__main__":
    r = ChatRunner()
    r.run()

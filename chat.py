from runner import Runner


class ChatRunner(Runner):
    desc = "Basic Chat"

    def run(self):
        while True:
            new_message = {"role": "assistant", "content": ""}
            completion = self.chat_completion(stream=True)
            for chunk in completion:
                s = chunk.choices[0].delta.content # type: ignore
                print(s or "", end="", flush=True)
                if s: new_message["content"] += s

            print()
            self.messages.append(new_message)
            print()

            q = input("> ")
            if q in [':q', ':x', ':quit', ':exit', 'bye']: break
            self.messages.append({"role": "user", "content": q})


if __name__ == "__main__":
    r = ChatRunner()
    r.run()

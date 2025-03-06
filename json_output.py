import json
from rich import print
from runner import Runner


class JSONOutputRunner(Runner):
    desc = "JSON Output"

    def run(self):
        self.system_prompt = """
        The user will provide some exam text. Please parse the "question" and "answer" and output them in JSON format.

        EXAMPLE INPUT:
        Which is the highest mountain in the world? Mount Everest.

        EXAMPLE JSON OUTPUT:
        {
            "question": "Which is the highest mountain in the world?",
            "answer": "Mount Everest"
        }
        """

        q = "Which is the longest river in the world? The Nile River."

        self.messages = [{"role": "system", "content": self.system_prompt},
                         {"role": "user", "content": q}]

        # `response_format` for DeepSeek, Qwen
        json_object = {
            "type": "json_object",
        }

        # `response_format` for Qwen, LM Studio API
        json_schema = {
            "type": "json_schema",
            "json_schema": {
                "name": "session",
                "schema": {
                    "type": "object",
                    "properties": {
                        "question": {"type": "string"},
                        "answer": {"type": "string"},
                    },
                    "required": ["question", "answer"],
                },
                "required": ["session"],
            }
        }

        completion = self.client.chat.completions.create(
            model=self.model_id,
            messages=self.messages, # type: ignore
            response_format=json_object # type: ignore
        )

        s = completion.choices[0].message.content
        print(s)
        if s: print(json.loads(s))


if __name__ == "__main__":
    r = JSONOutputRunner()
    r.run()

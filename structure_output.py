import json
from rich import print
from runner import Runner


system_message = """
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


class StructureOutputRunner(Runner):
    def _run_with_response_format(self, response_format):
        self.messages = [{"role": "system", "content": system_message},
                         {"role": "user", "content": q}]

        completion = self.client.chat.completions.create(
            model=self.model_id,
            messages=self.messages, # type: ignore
            response_format=response_format # type: ignore
        )

        s = completion.choices[0].message.content
        print(s)
        if s: print(json.loads(s))


class JSONObjectRunner(StructureOutputRunner):
    desc = "Structured Output Type 1"

    def run(self):
        self._run_with_response_format(json_object)


class JSONSchemaRunner(StructureOutputRunner):
    desc = "Structured Output Type 2"

    def run(self):
        self._run_with_response_format(json_schema)


if __name__ == "__main__":
    r = JSONObjectRunner()
    r.run()

    r = JSONSchemaRunner()
    r.run()

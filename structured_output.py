import json
from rich import print

from mal.openai.client import append_message, chat_completion_chunk_content

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


class StructuredOutputRunner(Runner):
    def _run_with_response_format(self, response_format):
        messages = []
        append_message(messages, "system", system_message)
        append_message(messages, "user", q)

        completion = self.create_chat_completion(
            messages,
            stream=True,
            response_format=response_format
        )

        result_output = ""
        for chunk in completion:
            s = chat_completion_chunk_content(chunk)
            print(s or "", end="", flush=True)
            if s: result_output += s

        if result_output: print(json.loads(result_output))


class JSONObjectRunner(StructuredOutputRunner):
    description = "Structured Output Type 1"

    def run(self):
        self._run_with_response_format(json_object)


class JSONSchemaRunner(StructuredOutputRunner):
    description = "Structured Output Type 2"

    def run(self):
        self._run_with_response_format(json_schema)


if __name__ == "__main__":
    r = JSONObjectRunner()
    r.run()

    r = JSONSchemaRunner()
    r.run()

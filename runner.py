import os
from abc import ABC, abstractmethod
from openai import OpenAI, Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk
from providers import Provider, default_provider, default_model_type


class Runner(ABC):
    description = "Abstract"

    def __init__(self, provider: Provider=default_provider) -> None:
        self.provider = provider
        self.client = OpenAI(api_key=provider.api_key, base_url=provider.base_url)
        if provider.beta_base_url:
            self.client_beta = OpenAI(api_key=provider.api_key, base_url=provider.beta_base_url)
        self.model_id = self.model_id_from_type(default_model_type)

        self.welcome_message = "Introduce yourself to someone opening this program for the first time. Be concise."
        self.system_message = "You are a helpful assistant."
        self.temperature = 0.7
        self.messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": self.welcome_message},
        ]

    def model_id_from_type(self, model_type: str=default_model_type) -> str:
        match model_type:
            case "coder": return self.provider.coder_model_id
            case "reasoner": return self.provider.reasoner_model_id
            case _: return self.provider.chat_model_id

    def get_models(self):
        return self.client.models.list()

    def simple_chat_completion(self, q: str, beta: bool=False, model_type: str=default_model_type) -> ChatCompletion:
        c = self.client_beta if beta and self.client_beta else self.client
        model_id = self.model_id_from_type(model_type)
        return c.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": q}
            ],
            temperature=self.temperature
        )

    def chat_completion(self, beta: bool=False, model_type: str=default_model_type, stream=False) -> ChatCompletion | Stream[ChatCompletionChunk]:
        c = self.client_beta if beta and self.client_beta else self.client
        model_id = self.model_id_from_type(model_type)

        return c.chat.completions.create(
            model=model_id,
            messages=self.messages, # type: ignore
            temperature=self.temperature,
            stream=stream
        )

    def reasoning_completion(self, stream: bool=False) -> ChatCompletion | Stream[ChatCompletionChunk]:
        model_id = self.model_id_from_type("reasoner")
        assert model_id
        return self.client.chat.completions.create(
            model=model_id,
            messages=self.messages, # type: ignore
            stream=stream
        )

    def clear_messages(self):
        self.messages.clear()

    def add_message(self, role, message):
        self.messages.append({"role": role, "content": message})

    @abstractmethod
    def run(self):
        pass

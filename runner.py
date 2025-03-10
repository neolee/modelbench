import os
from abc import ABC, abstractmethod
from openai import OpenAI, Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk
from mal.providers import Provider, default_provider


class Runner(ABC):
    description = "Abstract"

    def __init__(self, provider: Provider=default_provider) -> None:
        self.provider = provider

        self.client = OpenAI(api_key=provider.api_key, base_url=provider.base_url)
        if provider.beta_base_url:
            self.client_beta = OpenAI(api_key=provider.api_key, base_url=provider.beta_base_url)

        self.model_id = provider.model_id
        self.chat_model_id = provider.chat_model_id
        self.coder_model_id = provider.coder_model_id
        self.reasoner_model_id = provider.reasoner_model_id

        self.welcome_message = "Introduce yourself to someone opening this program for the first time. Be concise."
        self.system_message = "You are a helpful assistant."
        self.temperature = 0.7

        self.messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": self.welcome_message},
        ]

    def get_models(self):
        return self.client.models.list()

    def chat_completion(self, beta: bool=False, stream=False) -> ChatCompletion | Stream[ChatCompletionChunk]:
        c = self.client_beta if beta and self.client_beta else self.client

        return c.chat.completions.create(
            model=self.model_id,
            messages=self.messages, # type: ignore
            temperature=self.temperature,
            stream=stream
        )

    def reasoning_completion(self, stream: bool=False) -> ChatCompletion | Stream[ChatCompletionChunk]:
        return self.client.chat.completions.create(
            model=self.reasoner_model_id,
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

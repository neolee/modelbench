import os
from abc import ABC, abstractmethod

from mal.providers import Provider, default_provider, default_model_type
from mal.openai.model import client_by_provider, create_completion, create_chat_completion


class Runner(ABC):
    description = "Abstract"

    def __init__(self, provider: Provider=default_provider):
        self.provider = provider

        self.client = client_by_provider(provider)
        if provider.beta_base_url:
            self.client_beta = client_by_provider(provider, is_beta=True)

        self.model_name = provider.model_id
        self.chat_model_name = provider.chat_model_id
        self.coder_model_name = provider.coder_model_id
        self.reasoner_model_name = provider.reasoner_model_id

    def create_completion(self, is_beta=False, model_type=default_model_type, **kwargs):
        client = self.client_beta if is_beta and self.client_beta else self.client
        model_name = self.provider.model_id_from_type(model_type)
        return create_completion(client, model_name, **kwargs)

    def create_chat_completion(self, messages, is_beta=False, model_type=default_model_type, **kwargs):
        client = self.client_beta if is_beta and self.client_beta else self.client
        model_name = self.provider.model_id_from_type(model_type)
        return create_chat_completion(client, model_name, messages, **kwargs)

    def get_models(self):
        return self.client.models.list()

    @abstractmethod
    def run(self):
        pass

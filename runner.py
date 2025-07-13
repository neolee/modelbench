from abc import ABC, abstractmethod

import mal.openai.client as c


class Runner(ABC):
    description = "Abstract"

    def __init__(self, model):
        self.model = model
        self.provider = model.provider

        self.client = c.client_by_provider(self.provider)
        if self.provider.beta_base_url:
            self.client_beta = c.client_by_provider(self.provider, is_beta=True)

        self.model_name = model.model_name

    def create_completion(self, is_beta=False, **kwargs):
        client = self.client_beta if is_beta and self.client_beta else self.client
        return c.create_completion(client, self.model_name, **kwargs)

    def create_chat_completion(self, messages, is_beta=False, **kwargs):
        client = self.client_beta if is_beta and self.client_beta else self.client
        return c.create_chat_completion(client, self.model_name, messages, **kwargs)

    def get_models(self):
        return self.client.models.list()

    @abstractmethod
    def run(self):
        pass

from abc import ABC, abstractmethod

import models as m


class Runner(ABC):
    name = "Abstract"

    def __init__(self, model=m.default):
        self.model = model

    def create_completion(self, is_beta=False, **kwargs):
        self.model.set_mode(is_beta)
        return self.model.create_completion(**kwargs)

    def create_chat_completion(self, messages, is_beta=False, **kwargs):
        self.model.set_mode(is_beta)
        return self.model.create_chat_completion(messages, **kwargs)

    def get_models(self):
        return self.model.client.models.list()

    @abstractmethod
    def run(self):
        pass

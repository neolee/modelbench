import os
import rtoml


class Provider:
    def __init__(self, config: dict) -> None:
        self.description = config["description"]
        self.api_key = os.environ.get(config["api_key_name"])
        self.base_url = config["base_url"]
        self.beta_base_url = config["beta_base_url"]
        self.chat_model_id = config["chat_model_id"]
        self.coder_model_id = config["coder_model_id"]
        self.reasoner_model_id = config["reasoner_model_id"]


with open("providers.toml", "r") as f:
    data = rtoml.load(f)

default_provider_name: str = data["default"]["provider"]
default_model_type: str = data["default"]["model_type"]

def provider_by_name(name: str=default_provider_name) -> Provider:
    config: dict = data["providers"][name]
    return Provider(config)

default_provider = provider_by_name()

providers = []
for name in data["providers"]:
    providers.append(provider_by_name(name))

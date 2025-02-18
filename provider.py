import os
from rich import print
from openai import OpenAI
from openai.types.chat import ChatCompletion


class Provider:
    def __init__(self, api_key_name, base_url, beta_base_url,
                 chat_model_id, coder_model_id, reasoner_model_id) -> None:
        self.api_key_name = api_key_name
        self.base_url = base_url
        self.beta_base_url = beta_base_url
        self.chat_model_id = chat_model_id
        self.coder_model_id = coder_model_id
        self.reasoner_model_id = reasoner_model_id


deepseek = Provider(
    "DEEPSEEK_API_KEY",
    "https://api.deepseek.com",
    "https://api.deepseek.com/beta",
    "deepseek-chat",
    "",
    "deepseek-reasoner"
)

aliyun_qwen = Provider(
    "ALIYUN_API_KEY",
    "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "qwen-max-latest",
    "qwen-coder-plus-latest",
    ""
)

aliyun_deepseek = Provider(
    "ALIYUN_API_KEY",
    "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "deepseek-v3",
    "",
    "deepseek-r1"
)

provider = aliyun_qwen


api_key = os.environ.get(provider.api_key_name)
client = OpenAI(api_key=api_key, base_url=provider.base_url)
if provider.beta_base_url: client_beta = OpenAI(api_key=api_key, base_url=provider.beta_base_url)
model_id = provider.chat_model_id

def model_id_from_type(model_type: str="chat") -> str:
    match model_type:
        case "coder": return provider.coder_model_id
        case "reasoner": return provider.reasoner_model_id
        case _: return provider.chat_model_id

system_message = "You are a helpful assistant."


def simple_chat_completion(q, sm) -> ChatCompletion:
    return client.chat.completions.create(
        model=model_id,
        messages=[
            {"role": "system", "content": sm},
            {"role": "user", "content": q}
        ],
        temperature=0.7
    )

def chat_completion(history, beta=False, model_type="chat", temperature=0.7, stream=False) -> ChatCompletion:
    c = client_beta if beta else client
    model_id = model_id_from_type(model_type)

    return c.chat.completions.create(
        model=model_id,
        messages=history, # type: ignore
        temperature=temperature,
        stream=stream
    )


if __name__ == "__main__":
    print(client.models.list())

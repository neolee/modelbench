class Provider:
    def __init__(self, desc, api_key_name, base_url, beta_base_url,
                 chat_model_id, coder_model_id, reasoner_model_id) -> None:
        self.desc = desc
        self.api_key_name = api_key_name
        self.base_url = base_url
        self.beta_base_url = beta_base_url
        self.chat_model_id = chat_model_id
        self.coder_model_id = coder_model_id
        self.reasoner_model_id = reasoner_model_id


deepseek = Provider(
    "DeepSeek Official",
    "DEEPSEEK_API_KEY",
    "https://api.deepseek.com",
    "https://api.deepseek.com/beta",
    "deepseek-chat",
    "deepseek-chat",
    "deepseek-reasoner"
)

aliyun_qwen = Provider(
    "Qwen Official (Aliyun)",
    "ALIYUN_API_KEY",
    "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "qwen-max-latest",
    "qwen-coder-plus-latest",
    "qwq-plus-latest"
)

aliyun_deepseek = Provider(
    "DeepSeek (Aliyun)",
    "ALIYUN_API_KEY",
    "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "deepseek-v3",
    "deepseek-v3",
    "deepseek-r1"
)

ecnu_deepseek = Provider(
    "DeepSeek-R1 (ECNU)",
    "ECNU_API_KEY",
    "https://chat.ecnu.edu.cn/open/api/v1",
    "https://chat.ecnu.edu.cn/open/api/v1",
    "ecnu-max",
    "",
    "ecnu-reasoner"
)

providers = [deepseek, aliyun_qwen, aliyun_deepseek, ecnu_deepseek]
default_provider = aliyun_qwen

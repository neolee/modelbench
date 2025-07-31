import mal.providers as mal
from mal.openai.client import model_by_provider, model_by_provider_with_model


deepseek = model_by_provider(mal.deepseek_provider, description="DeepSeek-V3")
deepseek_reasoner = model_by_provider(mal.deepseek_provider, "reasoner", "DeepSeek-R1")

qwen = model_by_provider(mal.qwen_provider, description="Qwen Plus")
qwen_coder = model_by_provider(mal.qwen_provider, "coder", "Qwen-Coder Plus")

kimi_k2 = model_by_provider(mal.moonshot_provider, description="Kimi K2")
kimi_reasoner = model_by_provider(mal.moonshot_provider, "reasoner", "Kimi Thinking")

openrouter = model_by_provider(mal.openrouter_provider, description="Gemini 2.5 Flash Preview")
openrouter_gemini_flash = model_by_provider_with_model(mal.openrouter_provider, "google/gemini-2.5-flash", "Gemini 2.5 Flash")
openrouter_gemini_pro = model_by_provider_with_model(mal.openrouter_provider, "google/gemini-2.5-pro", "Gemini 2.5 Pro")
openrouter_grok = model_by_provider_with_model(mal.openrouter_provider, "x-ai/grok-4", "Grok 4")
openrouter_k2 = model_by_provider_with_model(mal.openrouter_provider, "moonshotai/kimi-k2", "Kimi K2")

local = model_by_provider(mal.local_provider, description="Qwen3-30B-A3B 2507")
local_reasoner = model_by_provider_with_model(mal.local_provider, "qwen3-thinking", "Qwen3-30B-A3B 2507 (Thinking)")
local_coder = model_by_provider_with_model(mal.local_provider, "qwen3-coder", "Qwen3-Coder-Flash")

lmstudio = model_by_provider(mal.lmstudio_provider, description="LM Studio Default")

ollama = model_by_provider(mal.ollama_provider, description="Ollama Default")

models = [deepseek, deepseek_reasoner, qwen, qwen_coder, kimi_k2,
          openrouter_gemini_flash, openrouter_gemini_pro, openrouter_grok,
          local, local_reasoner, local_coder, lmstudio]

default = deepseek

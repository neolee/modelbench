import mal.providers as mal
from mal.openai.client import model_by_provider, model_by_provider_with_model


deepseek = model_by_provider(mal.deepseek_provider, description="DeepSeek-V3")
deepseek_reasoner = model_by_provider(mal.deepseek_provider, "reasoner", "DeepSeek-R1")

qwen = model_by_provider(mal.qwen_provider, description="Qwen2.5-Max")
qwen_coder = model_by_provider(mal.qwen_provider, "coder", "Qwen2.5-Coder-Plus")
qwen_reasoner = model_by_provider(mal.qwen_provider, "reasoner", "QwQ-Plus")

kimi_k2 = model_by_provider(mal.moonshot_provider, description="Kimi K2")
kimi_reasoner = model_by_provider(mal.moonshot_provider, "reasoner", "Kimi Thinking")

openrouter = model_by_provider(mal.openrouter_provider, description="Gemini 2.5 Flash Preview")
openrouter_gemini_flash = model_by_provider_with_model(mal.openrouter_provider, "google/gemini-2.5-flash-preview-05-20", "Gemini 2.5 Flash Preview")
openrouter_gemini_flash_thinking = model_by_provider_with_model(mal.openrouter_provider, "google/gemini-2.5-flash-preview-05-20:thinking", "Gemini 2.5 Flash Preview (thinking)")
openrouter_gemini_pro = model_by_provider_with_model(mal.openrouter_provider, "google/gemini-2.5-pro-preview", "Gemini 2.5 Pro Preview")
openrouter_grok = model_by_provider_with_model(mal.openrouter_provider, "x-ai/grok-4", "Grok 4")
openrouter_k2 = model_by_provider_with_model(mal.openrouter_provider, "moonshotai/kimi-k2", "Kimi K2")

local = model_by_provider(mal.local_provider, description="Local Default")
local_qwen = model_by_provider_with_model(mal.local_provider, "qwen3", "Qwen3-30B-A3B")
local_qwen_nothink = model_by_provider_with_model(mal.local_provider, "qwen3-nothink", "Qwen3-30B-A3B (w/o Thinking)")
local_gemma = model_by_provider_with_model(mal.local_provider, "gemma-3", "Gemma-3-12B")
local_devstral = model_by_provider_with_model(mal.local_provider, "devstral", "Devstral-Small-2505")

lmstudio = model_by_provider(mal.lmstudio_provider, description="LM Studio Default")

ollama = model_by_provider(mal.ollama_provider, description="Ollama Default")

models = [deepseek, deepseek_reasoner, qwen, qwen_coder, qwen_reasoner, kimi_k2,
          openrouter_gemini_flash, openrouter_gemini_pro, openrouter_grok,
          local_qwen, local_qwen_nothink, local_gemma, local_devstral, lmstudio]

default = deepseek

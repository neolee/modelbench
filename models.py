from mal.adapter.openai import Model


deepseek_flash = Model("deepseek/deepseek-v4-flash", name="DeepSeek-V4-Flash")
deepseek_pro = Model("deepseek/deepseek-v4-pro", name="DeepSeek-V4-Pro")

qwen = Model("qwen/qwen3.6-plus", name="Qwen3.6 Plus")

kimi = Model("moonshot/kimi-k2-turbo-preview", name="Kimi K2")
kimi_reasoner = Model("moonshot/kimi-k2.6", name="Kimi K2.6")

glm = Model("zhipu/glm-5.1", name="GLM-5.1")

gpt = Model("openai", name="GPT-5.5")

openrouter_gemini_flash = Model("openrouter/google/gemini-3-flash-preview", name="Gemini 3 Flash")
openrouter_gemini_pro = Model("openrouter/google/gemini-3.1-pro-preview", name="Gemini 3.1 Pro")
openrouter_grok = Model("openrouter/x-ai/grok-4.1-fast", name="Grok 4.1 Fast")

local = Model("local/qwen3.6-nt", name="Qwen3.6-35B-A3B Non-thinking")
local_reasoner = Model("local/qwen3.6", name="Qwen3.6-35B-A3B")

omlx_qwen_35b = Model("omlx", "Qwen3.6-35B-A3B MLX")

models = [deepseek_flash, deepseek_pro, qwen, kimi, kimi_reasoner, glm, 
          gpt, openrouter_gemini_flash, openrouter_gemini_pro, openrouter_grok,
          local, local_reasoner, omlx_qwen_35b]

default = deepseek_flash

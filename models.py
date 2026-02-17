from mal.adapter.openai import Model


deepseek = Model("deepseek/deepseek-chat", name="DeepSeek-V3.2 (Non-thinking)")
deepseek_reasoner = Model("deepseek/deepseek-reasoner", name="DeepSeek-V3.2")

qwen = Model("qwen/qwen-plus-latest", name="Qwen Plus")
qwen_reasoner = Model("qwen/qwen3-max-2026-01-23", name="Qwen Max")
qwen_coder = Model("qwen/qwen3-coder-plus", name="Qwen-Coder Plus")

kimi = Model("moonshot/kimi-k2-turbo-preview", name="Kimi K2")
kimi_reasoner = Model("moonshot/kimi-k2.5", name="Kimi K2.5")

glm = Model("zhipu/glm-4.7", name="GLM-4.7")

gpt = Model("openai", name="GPT-5.2")

openrouter_gemini_flash = Model("openrouter/google/gemini-2.5-flash", name="Gemini 3 Flash")
openrouter_gemini_pro = Model("openrouter/google/gemini-3-pro-preview", name="Gemini 3 Pro")
openrouter_grok = Model("openrouter/x-ai/grok-4.1-fast", name="Grok 4.1 Fast")

local = Model("local/qwen3", name="Qwen3-30B-A3B 2507")
local_reasoner = Model("local/qwen3-thinking", name="Qwen3-30B-A3B 2507 (Thinking)")

models = [deepseek, deepseek_reasoner, qwen, qwen_reasoner, qwen_coder, kimi, kimi_reasoner, glm, 
          gpt, openrouter_gemini_flash, openrouter_gemini_pro, openrouter_grok,
          local, local_reasoner]

default = deepseek

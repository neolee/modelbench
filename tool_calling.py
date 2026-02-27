# function calling document from aliyun:
# https://help.aliyun.com/zh/model-studio/user-guide/qwen-function-calling

import json
from rich import print

from runner import Runner


## tool functions implementation
from amap import weather_info
from datetime import datetime

# query for weather condition
#   `arguments`: {"location": "Shanghai"}
def get_current_weather(location, **kwargs):
    info = weather_info(location)
    weather = info["lives"][0]["weather"] if info else "未知"

    return f"{location}今天天气是{weather}。"

# query for current time
def get_current_time(**kwargs):
    current_datetime = datetime.now()
    formatted_time = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return f"当前时间：{formatted_time}。"

# function mapper for convenience
function_mapper = {
    "get_current_weather": get_current_weather,
    "get_current_time": get_current_time
}


class ToolCallingRunner(Runner):
    name = "Tool Calling"

    def run(self):
        ## tools definition for language model
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_current_time",
                    "description": "当你想知道现在的时间时非常有用。",
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "required": []
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_current_weather",
                    "description": "当你想查询指定城市的天气时非常有用。",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "城市或县区，比如北京市、杭州市、余杭区等。",
                            }
                        },
                        "required": ["location"]
                    }
                }
            }
        ]

        ## system message and query
        system_message = """
        你是一个很有帮助的助手。
        如果用户提问关于天气的问题，请调用 ‘get_current_weather’ 函数；
        如果用户提问关于时间的问题，请调用 ‘get_current_time’ 函数。
        请以友好的语气回答问题。
        """

        messages = [
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": "上海天气"
            }
        ]

        def function_call():
            completion = self.create_chat_completion(
                messages,
                tools=tools,
                parallel_tool_calls=True # `tool_call_id` is required by deepseek
            )
            print(self.model.chat_completion_message(completion))
            return completion

        completion = function_call()
        tool_calls = self.model.chat_completion_tool_calls(completion)
        if tool_calls:
            tool_call = tool_calls[0]
            function_name = tool_call.function.name
            arguments_string = tool_call.function.arguments

            f = function_mapper[function_name]
            args = json.loads(arguments_string)
            output = f(**args)

            message = self.model.chat_completion_message(completion)
            messages.append(message)
            messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": output})

            # feed tool's result to model to get more human-like generation
            result = self.model.create_chat_completion_clean(
                messages,
                stream=False,
                tools=tools,
            )
            print(result["content"])


if __name__ == "__main__":
    r = ToolCallingRunner()
    r.run()

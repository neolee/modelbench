# function calling document from aliyun;
# https://help.aliyun.com/zh/model-studio/user-guide/qwen-function-calling

import json
from rich import print
from provider import model_id, client


## tool functions implementation
import random
from datetime import datetime

# TODO query for weather condition
#   `arguments`: {"location": "Shanghai"}
def get_current_weather(arguments):
    weather_conditions = ["晴天", "多云", "雨天"]
    random_weather = random.choice(weather_conditions)
    location = arguments["location"]
    return f"{location}今天天气是{random_weather}。"

# query for current time
def get_current_time():
    current_datetime = datetime.now()
    formatted_time = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return f"当前时间：{formatted_time}。"

# function mapper for convenience
function_mapper = {
    "get_current_weather": get_current_weather,
    "get_current_time": get_current_time
}


## tools definition for language model
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "当你想知道现在的时间时非常有用。",
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
sm = """
你是一个很有帮助的助手。
如果用户提问关于天气的问题，请调用 ‘get_current_weather’ 函数；
如果用户提问关于时间的问题，请调用 ‘get_current_time’ 函数。
请以友好的语气回答问题。
"""

messages = [
    {
        "role": "system",
        "content": sm,
    },
    {
        "role": "user",
        "content": "上海天气"
    }
]

def function_call():
    completion = client.chat.completions.create(
        model=model_id,
        messages=messages, # type: ignore
        tools=tools, # type: ignore
        parallel_tool_calls=True
    )
    print(completion.choices[0].message.model_dump_json())
    return completion

completion = function_call()
if completion.choices[0].message.tool_calls:
    function_name = completion.choices[0].message.tool_calls[0].function.name
    arguments_string = completion.choices[0].message.tool_calls[0].function.arguments

    f = function_mapper[function_name]
    args = json.loads(arguments_string)

    if args == {}:
        output = f()
    else:
        output = f(args)

    messages.append(completion.choices[0].message) # type: ignore
    messages.append({"role": "tool", "content": output})

    completion = function_call()
    print(completion.choices[0].message.content)

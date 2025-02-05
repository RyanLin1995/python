import json
import os

from zhipuai import ZhipuAI

client = ZhipuAI(
    api_key=os.getenv("ZHIPUAI_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)


def find_product(sql_query):
    results = [
        {"name": "pen", "color": "blue", "price": 1.99},
        {"name": "Banana", "color": "red", "price": 1.78},
    ]
    return results


functions = [
    {
        "type": "function",
        "function": {
            "name": "find_product",
            "description": "Get a list of products from a sql query",
            "parameters": {
                "type": "object",
                "properties": {
                    "sql_query": {
                        "type": "string",
                        "description": "A SQL query",
                    }
                },
                "required": ["sql_query"],
            },
        },
    }
]
user_questions = "I need the top 2 products where the price is less than 2.00"
message = [
    {"role": "user", "content": user_questions},
]
response = client.chat.completions.create(
    model="GLM-4-Flash", messages=message, tools=functions
)
response_message = response.choices[0].message.model_dump()
tool_call = response.choices[0].message.tool_calls[0]
message.append(response_message)

# 调用函数
function_args = json.loads(tool_call.function.arguments)
products = find_product(function_args.get("sql_query"))

# 将函数的响应附加到信息中
message.append(
    {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": f"{json.dumps(products)}",
    }
)
# 将函数的响应格式化为自然语言
response = client.chat.completions.create(
    model="GLM-4-Flash", messages=message, tools=functions
)
print(response.choices[0].message.content)

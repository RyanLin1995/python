import json
import os
import sqlalchemy
import pandas as pd

from zhipuai import ZhipuAI

client = ZhipuAI(
    api_key=os.getenv("ZHIPUAI_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)


def find_tn_info(sql_query):
    db_conn = sqlalchemy.create_engine(
        "mysql+pymysql://root:Abcd12345@127.0.0.1:3306/sea_platform"
    )
    results = pd.read_sql(sql_query, db_conn)
    return results.to_json()


functions = [
    {
        "type": "function",
        "function": {
            "name": "find_tn_info",
            "description": "Get a list of info from a sql query, the table is bpa_info",
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
user_questions = "I need info which tn is 1062292744"
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
ret = find_tn_info(function_args.get("sql_query"))

# 将函数的响应附加到信息中
message.append(
    {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": f"{json.dumps(ret)}",
    }
)
# 将函数的响应格式化为自然语言
response = client.chat.completions.create(
    model="GLM-4-Flash", messages=message, tools=functions
)
print(response.choices[0].message.content)

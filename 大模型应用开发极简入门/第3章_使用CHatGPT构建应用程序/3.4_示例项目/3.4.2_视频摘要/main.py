import os
from zhipuai import ZhipuAI

client = ZhipuAI(
    api_key=os.getenv("ZHIPUAI_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

with open("test.txt", "r") as f:
    text = f.read()

response = client.chat.completions.create(
    model="GLM-4-Flash",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {"role": "user", "content": "Summarize the following text"},
        {"role": "assistant", "content": "Yes"},
        {"role": "user", "content": text},
    ],
)
print(response.choices[0].message.content)

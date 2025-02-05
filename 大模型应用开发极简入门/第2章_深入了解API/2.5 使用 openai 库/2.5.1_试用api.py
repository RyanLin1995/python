import os

from zhipuai import ZhipuAI

client = ZhipuAI(
    api_key=os.getenv("ZHIPUAI_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)
chat_completion = client.chat.completions.create(
    model="GLM-4V-Plus",
    messages=[
        {"role": "system", "content": "You are a helpful teacher."},
        {
            "role": "user",
            "content": "Are there other measures than time complexity for an algorithm?",
        },
        {
            "role": "assistant",
            "content": "Yes, there are other measures besides time complexity for an algorithm, such as space complexity.",
        },
        {"role": "user", "content": "What is it?"},
    ],
)
print(chat_completion)

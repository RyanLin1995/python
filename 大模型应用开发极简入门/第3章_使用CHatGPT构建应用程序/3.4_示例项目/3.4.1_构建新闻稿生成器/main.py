import os
from typing import List

from zhipuai import ZhipuAI

client = ZhipuAI(
    api_key=os.getenv("ZHIPUAI_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

prompt_role = "You are a assistant for journalists. Your task is to write articles, based on the FACTS that are given to you. You should respect the instructions: the TONE, the LENGTH, and the STYLE."


def ask_chatgpt(message):
    response = client.chat.completions.create(
        model="GLM-4-Flash",
        messages=message,
        stream=False,
    )
    return response.choices[0].message.model_dump().get("content")


def assist_journalist(facts: List[str], tone: str, length_words: int, style: str):
    facts = ", ".join(facts)
    prompt = f"""{prompt_role}
    * FACTS: {facts}
    * TONE: {tone}
    * LENGTH: {length_words} words 
    * STYLE: {style}"""
    return ask_chatgpt([{"role": "user", "content": prompt}])


if __name__ == "__main__":
    facts = [
        "The United States is the world's largest country by land area.",
        "The United States has the largest population of any country in the world.",
    ]
    tone = "formal"
    length_words = 100
    style = "informative"
    print(assist_journalist(facts, tone, length_words, style))

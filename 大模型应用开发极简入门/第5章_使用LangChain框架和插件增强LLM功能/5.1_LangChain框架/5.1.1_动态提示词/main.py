import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

template = """Question: {question}
Let's think step by step.
Answer: """

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = ChatOpenAI(
    api_key=os.getenv("ZHIPUAI_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    model="GLM-4-Flash",
    temperature=0,
)
llm_chain = prompt | llm
question = "What is the population of the capital of the country where the Olympic Games were held in 2016"
print(llm_chain.invoke({"question": question}).content)

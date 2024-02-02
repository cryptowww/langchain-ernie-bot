#!/usr/bin/env python
# -*- coding: utf-8 -*-

# quickstart_QianfanLLM.py

import settings
from langchain_community.llms import QianfanLLMEndpoint

llm = QianfanLLMEndpoint(
        streaming=True,
        model="ERNIE-Bot-turbo",
        verbose=True,
        temperature=0.9,
        top_p=0.9,
    )

# 1
print("############--No.1--#################")
response = llm.invoke("你是谁")
print(response)


# 2

print("############--No.2--#################")

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "you are world technical documentation writer."),
    ("user","{input}")
])

output_parser = StrOutputParser()


chain = prompt | llm | output_parser

response = chain.invoke({"input": "how can langsmith help with testing?"})
print(response)

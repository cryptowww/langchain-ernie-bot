#!/usr/bin/env python
# -*- coding: utf-8 -*-

# runnableBranch.py

import sys
sys.path.append("..")
import settings

#from langchain.chat_models import QianfanChatEndpoint
from langchain_community.llms import QianfanLLMEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnableBranch, RunnableLambda


model = QianfanLLMEndpoint(model = "ERNIE-Bot")
chain = (
    PromptTemplate.from_template(
        """Given the user question below, classify it as either being about `LangChain`, `Anthropic`, or `Other`.

Do not respond with more than one word.

<question>
{question}
</question>

Classification:"""
    )
    | model
    | StrOutputParser()
)

response = chain.invoke({"question": "how do I call Anthropic?"})
print(response)



##################################################################
langchain_chain = (
    PromptTemplate.from_template(
        """You are an expert in langchain. \
Always answer questions starting with "As Harrison Chase told me". \
Respond to the following question:

Question: {question}
Answer:"""
    )
    | model
)
anthropic_chain = (
    PromptTemplate.from_template(
        """You are an expert in anthropic. \
Always answer questions starting with "As Dario Amodei told me". \
Respond to the following question:

Question: {question}
Answer:"""
    )
    | model
)
general_chain = (
    PromptTemplate.from_template(
        """Respond to the following question:

Question: {question}
Answer:"""
    )
    | model
)

branch = RunnableBranch(
    (lambda x: "anthropic" in x["topic"].lower(), anthropic_chain),
    (lambda x: "langchain" in x["topic"].lower(), langchain_chain),
    general_chain,
)

full_chain = {"topic": chain, "question": lambda x: x["question"]} | branch

response = full_chain.invoke({"question": "how do I use Anthropic?"})
print(response)
response = full_chain.invoke({"question": "how do I use LangChain?"})
print(response)
response = full_chain.invoke({"question": "whats 2 + 2"})
print(response)

#######################custom-function#############
def route(info):
    if "anthropic" in info["topic"].lower():
        return anthropic_chain
    elif "langchain" in info["topic"].lower():
        return langchain_chain
    else:
        return general_chain

full_chain = {"topic": chain, "question": lambda x: x["question"]} | RunnableLambda(
    route
)


response = full_chain.invoke({"question": "how do I use Anthropic?"})
print(response)
response = full_chain.invoke({"question": "how do I use LangChain?"})
print(response)
response = full_chain.invoke({"question": "whats 2 + 2"})
print(response)




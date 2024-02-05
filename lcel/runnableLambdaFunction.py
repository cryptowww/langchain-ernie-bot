#!/usr/bin/env python
# -*- coding: utf-8 -*-

# runnableLambdaFunction.py

import sys
sys.path.append("..")
import settings

from operator import itemgetter
from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda


model = QianfanChatEndpoint(model = "ERNIE-Bot")

def length_function(text):
    return len(text)


def _multiple_length_function(text1, text2):
    return len(text1) * len(text2)


def multiple_length_function(_dict):
    return _multiple_length_function(_dict["text1"], _dict["text2"])


prompt = ChatPromptTemplate.from_template("what is {a} + {b}")
chain = (
    {
        "a": itemgetter("foo") | RunnableLambda(length_function),
        "b": {"text1": itemgetter("foo"), "text2": itemgetter("bar")}
        | RunnableLambda(multiple_length_function),
    }
    | prompt
    | model
)

response = chain.invoke({"foo": "hello", "bar": "world"})
print(response)

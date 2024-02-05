#!/usr/bin/env python
# -*- coding: utf-8 -*-

# runnableParallelizeSetup.py

import sys
sys.path.append("..")
import settings

from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel


model = QianfanChatEndpoint(model = "ERNIE-Bot")

joke_chain = ChatPromptTemplate.from_template("tell me a joke about {topic}") | model

poem_chain = (ChatPromptTemplate.from_template("write a 2-line poem about {topic}") | model )

map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)

response = map_chain.invoke({"topic": "cat"})
print(response)


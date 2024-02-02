#!/usr/bin/env python
# -*- coding: utf-8 -*-

# getstarted.py

import sys
sys.path.append('..')
import settings

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import QianfanChatEndpoint

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = QianfanChatEndpoint(model="ERNIE-Bot")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

response = chain.invoke({"topic": "ice cream"})

print(response)

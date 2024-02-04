#!/usr/bin/env python
# -*- coding: utf-8 -*-

# getstarted.py

import sys
sys.path.append('..')
import settings

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import QianfanChatEndpoint

# define the prompt
prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
## invoke the prompt
prompt_value = prompt.invoke({"topic": "ice cream"})
print(prompt_value)
prompt_str = prompt_value.to_string()
print(prompt_str)
prompt_msg = prompt_value.to_messages()
print(prompt_msg)


# define the model
model = QianfanChatEndpoint(model="ERNIE-Bot")
## invoke the model
message = model.invoke(prompt_value)
print(message)

# define the output parser
output_parser = StrOutputParser()
## invoke the output parser
out_str = output_parser.invoke(message)
print(out_str)

chain = prompt | model | output_parser

response = chain.invoke({"topic": "ice cream"})

print(response)

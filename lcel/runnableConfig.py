#!/usr/bin/env python
# -*- coding: utf-8 -*-

# runnableConfig.py

import sys
sys.path.append("..")
import settings

from operator import itemgetter
import json
from langchain_community.llms import QianfanLLMEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableConfig, RunnableLambda
from langchain.callbacks import get_openai_callback

model = QianfanLLMEndpoint(model = "ERNIE-Bot")

def parse_or_fix(text: str, config: RunnableConfig):
    fixing_chain = (
        ChatPromptTemplate.from_template(
            "Fix the following text:\n\n```text\n{input}\n```\nError: {error}"
            " Don't narrate, just respond with the fixed data."
        )
        | model
        | StrOutputParser()
    )
    for _ in range(3):
        try:
            return json.loads(text)
        except Exception as e:
            text = fixing_chain.invoke({"input": text, "error": e}, config)
    return "Failed to parse"

with get_openai_callback() as cb:
    output = RunnableLambda(parse_or_fix).invoke(
        "{foo: bar}", {"tags": ["my-tag"], "callbacks": [cb]}
    )
    print(output)
    print(cb)

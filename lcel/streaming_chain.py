#!/usr/bin/env python
# -*- coding: utf-8 -*-

# streaming_chain.py

import sys
sys.path.append("..")
import settings

from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import asyncio


model = QianfanChatEndpoint(model = "ERNIE-Bot")
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
parser = StrOutputParser()
chain = prompt | model | parser

async def streamodel():
    async for s in chain.astream({"topic": "cat"}):
        print(s, end="|", flush=True)

#if __name__ == "__main__":
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(streamodel())
#    loop.close()
asyncio.run(streamodel())

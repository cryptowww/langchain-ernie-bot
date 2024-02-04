#!/usr/bin/env python
# -*- coding: utf-8 -*-

# streaming.py

import sys
sys.path.append("..")
import settings

from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.prompts import ChatPromptTemplate
import asyncio


model = QianfanChatEndpoint(model = "ERNIE-Bot")
chunks = []

        
async def streamodel():
    async for s in model.astream("Hi, tell me something about yourself."):
        chunks.append(s)
        print(s.content, end="|", flush=True)

#if __name__ == "__main__":
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(streamodel())
#    loop.close()
asyncio.run(streamodel())

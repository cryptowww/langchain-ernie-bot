#!/usr/bin/env python
# -*- coding: utf-8 -*-

# gemini_test.py

import sys
sys.path.append('..')
import settings


from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke("Write a ballad about LangChain")
print(result.content)

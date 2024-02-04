#!/usr/bin/env python
# -*- coding: utf-8 -*-

# getstarted_retrieval.py

import sys
sys.path.append("..")
import settings

from langchain_community.chat_models import QianfanChatEndpoint
from langchain_community.embeddings import QianfanEmbeddingsEndpoint
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

# create a vectorstore from a list of texts
vectorstore = DocArrayInMemorySearch.from_texts(
    ["harrison worked at kensho", "bears like to eat honey"],
    embedding=QianfanEmbeddingsEndpoint(chunk_size=1000)
)
retriever = vectorstore.as_retriever()

# create a prompt
template = """Answer the question based only on the following context:
{context}, only output the place name and nothing others to output, don't repeat the original sentence.

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

# create a model
model = QianfanChatEndpoint()

# create a output parser
output_parser = StrOutputParser()


setup_and_retrieval = RunnableParallel({
    "context": retriever,
    "question": RunnablePassthrough()
})

chain = setup_and_retrieval | prompt | model | output_parser
response = chain.invoke("where did harrison work?")
print(response)

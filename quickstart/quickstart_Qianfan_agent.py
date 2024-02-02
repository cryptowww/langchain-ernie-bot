#!/usr/bin/env python
# -*- coding: utf-8 -*-

# quickstart_Qianfan_agent.py

import sys
sys.path.append('..')
import settings
from langchain_community.chat_models import QianfanChatEndpoint

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.embeddings import QianfanEmbeddingsEndpoint

from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor

llm = QianfanChatEndpoint(
        streaming=True,
        model="ERNIE-Bot-4",
        verbose=True,
        temperature=0.2,
        top_p=0.5,
    )

# 外部数据
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()

embeddings = QianfanEmbeddingsEndpoint()

###### max length 1000, here we 1use RecursiveCharacterTextSplitter to split the documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings,)
retriever = vector.as_retriever()

#document_chain = create_stuff_documents_chain(llm, prompt)

# tools
retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
)
search = TavilySearchResults()
tools = [retriever_tool, search]

# prompt
prompt = hub.pull("hwchase17/openai-functions-agent")

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# err here, there are no qianfan agent in the langchain hub. wo use hwchase17/openai-functions-agent instead,but no api-key
response = agent_executor.invoke({"input": "how can langsmith help with testing?"})

print(response["answer"])

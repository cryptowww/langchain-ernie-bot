#!/usr/bin/env python
# -*- coding: utf-8 -*-

# quickstart_Qianfan_Conversation_Retrieval.py

import settings
from langchain_community.llms import QianfanLLMEndpoint

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.embeddings import QianfanEmbeddingsEndpoint

from langchain_community.vectorstores import FAISS,Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain

llm = QianfanLLMEndpoint(
        streaming=True,
        model="ERNIE-Bot-4",
        verbose=True,
        temperature=0.9,
        top_p=0.9,
    )

#response = llm.invoke("write a funny joke.")
#print(response)


# 外部数据
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()

embeddings = QianfanEmbeddingsEndpoint()

###### max length 1000, here we 1use RecursiveCharacterTextSplitter to split the documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
documents = text_splitter.split_documents(docs)
#print(documents)
vector = FAISS.from_documents(documents, embeddings)

retriever = vector.as_retriever()

# take the whole history into acc1ount
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

chat_history = [
    HumanMessage(content= "Can LangSmith help test my LLM applications?"),
    AIMessage(content="Yes")
]

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the user's questions based on the below context:\n\n{context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    ])
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)


response = retrieval_chain.invoke({
    "chat_history": chat_history,
    "input": "Tell me How"
})

print(response["answer"])

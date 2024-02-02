#!/usr/bin/env python
# -*- coding: utf-8 -*-

# quickstart_Qianfan_retrieval.py

import sys
sys.path.append('..')
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

response = llm.invoke("write a funny joke.")
print(response)


# 外部数据
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()

embeddings = QianfanEmbeddingsEndpoint()
#embeddings = OllamaEmbeddings()

###### max length 1000, here we 1use RecursiveCharacterTextSplitter to split the documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=900)
documents = text_splitter.split_documents(docs)
#print(documents)
#vector = FAISS.from_documents(documents, embeddings)
# error code: 336003, err msg: embeddings max length per batch size is 1000, please check https://cloud.baidu.com/doc/WENXINWORKSHOP/s/tlmyncueh
vector = Chroma.from_documents(documents, embeddings,)


prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)

document_chain.invoke({
    "input": "how can langsmith help with testing?",
    "context": [Document(page_content="langsmith can let you visualize test results")]
})

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "how can langsmith help with testing?"})
print(response["answer"])

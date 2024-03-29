# LangChain example using ERNIE-Bot  

## Prepare

```shell

pip install langchain

pip install qianfan

```

## How to Save the API key safely

```shell

mv .env.sample .env

```

## Retriever

```shell
pip install beautifulsoup4

pip install faiss-cpu

```

## Qianfan supported Models

1. EB-turbo-AppBuilder
2. ERNIE-Bot
3. ERNIE-Bot-4
4. ERNIE-Bot-8k
5. ERNIE-Bot-turbo
6. ERNIE-Speed
7. Qianfan-Chinese-Llama-2-7B
8. Qianfan-BLOOMZ-7B-compressed
9. Qianfan-Chinese-Llama-2-13B
10. CodeLlama-7b-Instruct
11. Llama-2-7b-chat
12. Llama-2-13b-chat
13. Llama-2-70b-chat
14. ChatGLM2-6B-32K
15. BLOOMZ-7B
16. ChatLaw
17. XuanYuan-70B-Chat-4bit
18. Yi-34B-Chat
19. SQLCoder-7B
20. AquilaChat-7B

## Get the access_token of Qianfan

1. curl

```shell

curl -d "grant_type=client_credentials&client_id=QQ1WV....dWzhj21Q&client_secret=Ds3GFGS....iExKyz10d2qr" https://aip.baidubce.com/oauth/2.0/token

```

2. python

[Get the access_key of Qianfan](./quickstart/get_qianfan_access_token.py)

## to fix

Qianfan has not provide agent . so you can replace the model with openai , if you have a openai API_KEY.
[openAI agent](./quickstart/qianfan_agent.py) , [langserver](./quickstart/qianfan_LangServer.py) with openAI.

## quickstart

according the documention, I dev the following code:

1. LLM Chain

    - [LLM with Qianfan](./quickstart/qanfanLLM.py)
    - [Chat with Qianfan](./quickstart/qianfanChat.py)

2. Retrieval Chain

    - [Retrieval with Qianfan](./quickstart/qianfan_retrieval.py)
    - [Conversation Retrieval with Qianfan](./quickstart/qianfan_Conversation_Retrieval.py)

3. Agent

you can run the code with OpenAI, but it's Qianfan in the code.
    - [Agent](./quickstart/qianfan_agent.py)

4. LangServer

    - [LangServer](./quickstart/qianfan_LangServer.py)



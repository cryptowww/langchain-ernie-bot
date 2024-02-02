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

[Get the access_key of Qianfan](./get_qianfan_access_token.py)

## to fix

Qianfan has not provide agent . so you can replace the model with openai , if you have a openai API_KEY.
[openAI agent](./quickstart_Qianfan_agent.py) , [langserver](./quickstart_Qianfan_LangServer.py) with openAI.

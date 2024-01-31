from config import settings

from langchain.schema import (
        AIMessage,
        HumanMessage,
        )
from langchain_community.chat_models import QianfanChatEndpoint

chat_model = QianfanChatEndpoint(
        streaming=True,
        model="ERNIE-Bot-turbo",
        qianfan_ak=settings.ERNIBOT_API_Key,
        qianfan_sk=settings.ERNIBOT_API_SECRET,
        verbose=True,
        temperature=0.9,
        top_p=0.9,
    )

response = chat_model.invoke([
        HumanMessage(content="给我讲一个冷笑话")
    ])
print(response)

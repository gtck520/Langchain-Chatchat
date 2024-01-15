import json
from server.chat.personal_chat import personal_chat
from configs import VECTOR_SEARCH_TOP_K, MAX_TOKENS
import asyncio
from server.agent import model_container
from pydantic import BaseModel, Field

async def personal_chat(query: str):
    response = await personal_chat(query=query,
                                         model_name=model_container.MODEL.model_name,
                                         temperature=0.01, # Agent 搜索互联网的时候，温度设置为0.01
                                         history=[],
                                         top_k = VECTOR_SEARCH_TOP_K,
                                         max_tokens= MAX_TOKENS,
                                         prompt_name = "default",
                                         stream=False)

    contents = ""

    async for data in response: # 这里的data是一个json字符串
        data = json.loads(data)
        contents = data["answer"]
    return contents

def search_api(query: str):
    return asyncio.run(personal_chat(query))

class SearchApiInput(BaseModel):
    location: str = Field(description="从知识库api文档中寻找合适的接口查询")


if __name__ == "__main__":
    result = personal_chat("今天星期几")
    print("答案:",result)

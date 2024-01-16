import sys
sys.path.append(".")
import json
from server.chat.personal_chat import personal_chat
from configs import LLM_MODELS,TEMPERATURE, MAX_TOKENS
import asyncio
from server.agent import model_container
from pydantic import BaseModel, Field

async def personal_chat_iter(query: str):
    response= await personal_chat(query=query,
                                model_name=LLM_MODELS[0],
                                max_tokens= MAX_TOKENS,                                 
                                temperature=TEMPERATURE)    
    async for data in response.body_iterator: # 这里的data是一个json字符串
        data = json.loads(data)
        contents = data["answer"]

    return contents

def search_api(query: str):
    return asyncio.run(personal_chat_iter(query))

class SearchApiInput(BaseModel):
    location: str = Field(description="从知识库api文档中寻找合适的接口查询")


if __name__ == "__main__":
    result = search_api("陈康的用户信息，结果使用表格输出")
    print("答案:",result)

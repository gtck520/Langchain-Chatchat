
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from server.utils import wrap_done, get_ChatOpenAI
from langchain.chains import APIChain
from langchain.prompts import PromptTemplate
from server.utils import get_prompt_template
from server.ext_api import test
import asyncio
from langchain.callbacks import AsyncFinalIteratorCallbackHandler
import json
from typing import AsyncIterable

async def main():
    print("开始执行")
    async def chat_iterator() -> AsyncIterable[str]:
        print("异步执行")
        model = get_ChatOpenAI(
                    model_name="openai-api",
                    temperature=0.7,
                    # max_tokens=max_tokens,
                    # callbacks=callbacks,
                )
        api_response_template = get_prompt_template("personal_chat", "default")
        api_response_prompt = PromptTemplate.from_template(api_response_template)

        # headers = {"Authorization": f"Bearer {os.environ['TMDB_BEARER_TOKEN']}"}  headers=headers            
        chain_new = APIChain.from_llm_and_api_docs(llm=model, 
                                            api_docs=test.TEST_DOCS, 
                                            verbose=True,
                                            limit_to_domains=["https://restapi.amap.com"],
                                            api_response_prompt=api_response_prompt)

        # print(chain_new.run(
        #     "福州今天天气如何"
        # ))

        answer = await chain_new.arun({"question": "福州今天天气如何"})
        return json.dumps(
                    {"text": answer, "message_id": "message_id"},
                    ensure_ascii=False) 
    
    print(await chat_iterator())
    
if __name__ == "__main__":
    asyncio.run(main())

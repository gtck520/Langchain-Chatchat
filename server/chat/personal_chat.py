from urllib import response
from fastapi import Body
from fastapi.responses import StreamingResponse
from configs import LLM_MODELS, TEMPERATURE
from server.utils import wrap_done, get_ChatOpenAI
from langchain.chains import LLMChain
from langchain.chains import APIChain
from langchain.callbacks import AsyncIteratorCallbackHandler
from typing import AsyncIterable
import asyncio
import json
from langchain.prompts.chat import ChatPromptTemplate
from typing import List, Optional, Union
from server.chat.utils import History
from langchain.prompts import PromptTemplate
from server.utils import get_prompt_template
from server.memory.conversation_db_buffer_memory import ConversationBufferDBMemory
from server.db.repository import add_message_to_db
from server.callback_handler.conversation_callback_handler import ConversationCallbackHandler
from server.ext_api import test,payment


async def personal_chat(query: str = Body(..., description="用户输入", examples=["恼羞成怒"]),
               history: Union[int, List[History]] = Body([],
                                                         description="历史对话，设为一个整数可以从数据库中读取历史消息",
                                                         examples=[[
                                                             {"role": "user",
                                                              "content": "我们来玩成语接龙，我先来，生龙活虎"},
                                                             {"role": "assistant", "content": "虎头虎脑"}]]
                                                         ),
               model_name: str = Body(LLM_MODELS[0], description="LLM 模型名称。"),
               temperature: float = Body(TEMPERATURE, description="LLM 采样温度", ge=0.0, le=1.0),
               max_tokens: Optional[int] = Body(None, description="限制LLM生成Token数量，默认None代表模型最大值"),
               ):
    async def chat_iterator() -> AsyncIterable[str]:
        nonlocal history, max_tokens
        callback = AsyncIteratorCallbackHandler()
        callbacks = [callback]

        if isinstance(max_tokens, int) and max_tokens <= 0:
            max_tokens = None

        model = get_ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
            callbacks=callbacks,
        )


        api_url_template = get_prompt_template("personal_chat", "url")
        api_url_prompt = PromptTemplate.from_template(api_url_template)
        
        api_response_template = get_prompt_template("personal_chat", "response")
        api_response_prompt = PromptTemplate.from_template(api_response_template)

        headers = {"api-key":"7leVZ5NZ6WNhyr4WwIczKfdqvNC_2doq"}             
        chain_new = APIChain.from_llm_and_api_docs(llm=model, 
                                           api_docs=payment.PAYMENT_DOCS, 
                                           verbose=True,
                                           limit_to_domains=["http://127.0.0.1:8080"],
                                           headers=headers,
                                           api_response_prompt=api_response_prompt,
                                           api_url_prompt=api_url_prompt)
        
        # 无header的
        # chain_new = APIChain.from_llm_and_api_docs(llm=model, 
        #                                    api_docs=test.TEST_DOCS, 
        #                                    verbose=True,
        #                                    limit_to_domains=["https://restapi.amap.com"],
        #                                    api_response_prompt=api_response_prompt)
        #   chain = LLMChain(prompt=chat_prompt, llm=model, memory=memory)

        # Begin a task that runs in the background.
        answer = await chain_new.arun({"question": query})        
        yield json.dumps(
                    {"answer": answer},
                    ensure_ascii=False)       

    return StreamingResponse(chat_iterator(), media_type="text/event-stream")

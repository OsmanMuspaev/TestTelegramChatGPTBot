import asyncio
from openai import OpenAI
from config import OPENAI_API_KEY, GPT_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def _sync_generate(messages: list) -> str:
    response = client.responses.create(
        model=GPT_MODEL,
        input=messages
    )
    return response.output_text


async def generate_answer(messages: list) -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _sync_generate, messages)
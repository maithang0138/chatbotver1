import chainlit as cl
import openai
import os

# Lấy API key từ biến môi trường Railway
openai.api_key = os.getenv("OPENAI_API_KEY")

@cl.on_message
async def main(message: cl.Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Bạn là trợ lý AI thân thiện."},
                {"role": "user", "content": message.content}
            ]
        )

        reply = response.choices[0].message.content.strip()
        await cl.Message(content=reply).send()

    except Exception as e:
        await cl.Message(content=f"❌ Lỗi: {e}").send()

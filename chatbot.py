
import openai
from openai import OpenAI

client = OpenAI()

def llm_response(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

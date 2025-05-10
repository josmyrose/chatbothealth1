
import openai
from openai import OpenAI
import os

#client = OpenAI()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not set in environment.")

client = OpenAI(api_key=api_key)

def llm_response(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content


import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def llm_response(user_input):
    prompt = f"User reports the following symptoms: {user_input}. Ask clarifying questions if needed, and guide them to the prediction."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

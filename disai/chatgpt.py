import openai
from dotenv import load_dotenv
import os
load_dotenv()

def getanswer(question):
    openai.api_key = os.getenv("chat_gpt_key")

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role":
        "user",
        "content":
        question
    }])
    return completion.choices[0].message.content

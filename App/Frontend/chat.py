from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from instructions import Instructions

load_dotenv()

class Chat():
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.client.chats.create
        self.chat = self.client.chats.create(model="gemma-3-27b-it", config= types.GenerateContentConfig(temperature=0.1))
        self.instructions = Instructions()

    def post_message(self, question):
        full_prompt = f"""
            {self.instructions.get_instructions("04")}
            {self.instructions.get_instructions("01")}
            Pergunta: {question}
            """
        return self.chat.send_message(full_prompt).text


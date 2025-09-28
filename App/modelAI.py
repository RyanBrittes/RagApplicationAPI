from ragGenerate import RagGenerate
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

class Chat():
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.persona = """Sua função é agir como um tutor para alunos do curso de medicina 
        que estão aprendendo sobre Neurociências. Agir de maneira empática, acessível, 
        acolhedora e humana sempre respondendo com detalhes sobre o assunto para que os 
        alunos consigam tirar suas dúvidas com clareza"""
        self.chat = self.client.chats.create(model="gemma-3-1b-it", config={"temperature": 0.6})
        self.recovery = RagGenerate()

    def make_question(self):
        loop_control = True
        i = 0

        while loop_control:
            print("\nUser: ")
            question = input()

            if question == "sair":
                print("<-----SAINDO----->")
                break

            relevant_docs = self.recovery.compair_vector(question)

            context_text = ""
            if 'documents' in relevant_docs and relevant_docs['documents']:
                for doc_list in relevant_docs['documents']:
                    for doc in doc_list:
                        context_text += f"{doc}\n\n"

            full_prompt = f"""{self.persona}
                Responda com base nos seguintes documentos:
                {context_text}
                Pergunta: {question}
                """
            
            response = self.chat.send_message(full_prompt)

            print(f"\nTutor: {response.text}")
            i += 2

A = Chat()

A.make_question()

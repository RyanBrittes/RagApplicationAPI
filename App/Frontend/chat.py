from Backend.ragGenerate import RagGenerate
from menu import Menu
from personas import Personas
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

class Chat():
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.chat = self.client.chats.create(model="gemma-3-1b-it", config={"temperature": 0.6})
        self.recovery = RagGenerate()
        self.menu = Menu()
        self.personas = Personas()

    def talk_with_tutor(self):
        persona = self.personas.get_personas("01")

        i = 0

        print("\n*****Hora de falar com o tutor, diga quais são suas dúvidas aqui e se quiser sair é digitar ""sair"" a qualquer momento*****")

        while True:
            print("\nUser: ")
            question = input()

            if question == "sair":
                print("<-----SAINDO----->")
                self.menu.get_menu()

            relevant_docs = self.recovery.compair_vector(question)

            context_text = ""
            if 'documents' in relevant_docs and relevant_docs['documents']:
                for doc_list in relevant_docs['documents']:
                    for doc in doc_list:
                        context_text += f"{doc}\n\n"

            full_prompt = f"""{persona}
                Responda com base nos seguintes documentos:
                {context_text}
                Pergunta: {question}
                """
            
            response = self.chat.send_message(full_prompt)

            print(f"\nTutor: {response.text}")
            i += 2
    
    def make_exercises(self):
        persona = self.personas.get_personas("02")

        i = 0

        print("\n*****Hora de praticar com o tutor, descreva que tipo de exercícios quer exercitar e se quiser sair é digitar ""sair"" a qualquer momento*****")

        while True:
            print("\nUser: ")
            question = input()

            if question == "sair":
                self.menu.get_menu()

            relevant_docs = self.recovery.compair_vector(question)

            context_text = ""
            if 'documents' in relevant_docs and relevant_docs['documents']:
                for doc_list in relevant_docs['documents']:
                    for doc in doc_list:
                        context_text += f"{doc}\n\n"

            full_prompt = f"""{persona}
                Responda com base nos seguintes documentos:
                {context_text}
                Pergunta: {question}
                """
            
            response = self.chat.send_message(full_prompt)

            print(f"\nTutor: {response.text}")
            i += 2

    def make_specific_questions(self):
        persona = self.personas.get_personas("01")

        i = 0

        print("\n*****Hora de falar com o tutor sobre temas específicos, diga quais são suas dúvidas aqui e se quiser sair é digitar ""sair"" a qualquer momento*****")

        while True:
            print("\nUser: ")
            question = input()

            if question == "sair":
                self.menu.get_menu()

            relevant_docs = self.recovery.compair_vector(question)

            context_text = ""
            if 'documents' in relevant_docs and relevant_docs['documents']:
                for doc_list in relevant_docs['documents']:
                    for doc in doc_list:
                        context_text += f"{doc}\n\n"

            full_prompt = f"""{persona}
                Responda com base nos seguintes documentos:
                {context_text}
                Pergunta: {question}
                """
            
            response = self.chat.send_message(full_prompt)

            print(f"\nTutor: {response.text}")
            i += 2

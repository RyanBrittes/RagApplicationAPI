import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Backend.ragGenerate import RagGenerate
from personas import Personas
from google import genai
from dotenv import load_dotenv

load_dotenv()

class FlowChat():
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.chat = self.client.chats.create(model="gemma-3-1b-it", config={"temperature": 0.6})
        self.recovery = RagGenerate()
        self.personas = Personas()

    def get_menu(self):
        while True:
            print("\n*****Seja bem vindo!!*****")
            print("\nEscolha uma das seguintes opções para continuar: ")
            opt = input("""\n01 - Iniciar uma conversa com o tutor
                        \n02 - Solicitar a criação de uma lista de exercícios
                        \n03 - Tirar dúvidas sobre um tema específico
                        \n04 - Sair\n""")
            match opt:
                case "01":
                    self.talk_with_tutor("1")
                    break

                case "02":
                    self.talk_with_tutor("2")
                    break

                case "03":
                    self.talk_with_tutor("3")
                    break

                case "04":
                    print("\nAté breve!!")
                    break
                
                case _:
                    print("\nOpção não encontrada, tente novamente")
                    break
            break

    def talk_with_tutor(self, opt):

        if opt == "1":
            persona = self.personas.get_personas("01")
            print("\n*****Hora de falar com o tutor, diga quais são suas dúvidas aqui e se quiser sair é digitar ""sair"" a qualquer momento*****")
        
        if opt == "2":
            persona = self.personas.get_personas("02")
            print("\n*****Hora de praticar com o tutor, descreva que tipo de exercícios quer exercitar e se quiser sair é digitar ""sair"" a qualquer momento*****")
        
        if opt == "3":
            persona = self.personas.get_personas("03")
            print("\n*****Hora de falar com o tutor sobre temas específicos, diga quais são suas dúvidas aqui e se quiser sair é digitar ""sair"" a qualquer momento*****")
        i = 0
        
        while True:
            print("\nUser: ")
            question = input()

            if question == "sair":
                print("<-----SAINDO----->")
                self.get_menu()

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

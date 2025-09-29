from chat import Chat

class Menu():

    def __init__(self):
        self.chat = Chat()

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
                    self.chat.talk_with_tutor()

                case "02":
                    self.chat.make_exercises()

                case "03":
                    self.chat.make_specific_questions()

                case "04":
                    print("\nAté breve!!")
                    break
                
                case _:
                    print("\Opção não encontrada, tente novamente")

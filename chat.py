from google import genai

class Chat():
    def __init__(self):
        self.client = genai.Client(api_key="AIzaSyB1ExkeeicZvX5EbGgvC_bVtHlwsZyQZ6Y")
        self.chat = self.client.chats.create(model="gemma-3-1b-it", config={"temperature": 0.6})

    def make_question(self):
        loop_control = True
        i = 0

        while loop_control:
            print("\nUser: ")
            response = self.chat.send_message(input())

            if self.chat.get_history()[i].parts[0].text == "sair":
                print("<-----SAINDO----->")
                break

            print(response.text)
            i += 2

A = Chat()

A.make_question()

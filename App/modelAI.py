from ragGenerate import RagGenerate
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

#Loop criado para interagir de maneira contínua com a LLM
while True:
    looping = input("Se desejar fazer uma pergunta digite sim, porém se quiser sair digite qualquer coisa:\n")

    if looping != "sim":
        break
    else:
        recovery = RagGenerate()
        question = input("Digite sua pergunta: ")
        persona = input("Digite a persona: ")

        prompt = f"""Responda com base nos seguintes documentos:
            {recovery.compair_vector(question)}

            Pergunta: {question}
            """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                {"role": "system", "content": persona},
                {"role": "user", "content": prompt}
            ]
        )

        print("***\n" + response['message']['content'] + "\n***")
        
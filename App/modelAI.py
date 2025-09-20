from ragGenerate import RagGenerate
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

#Loop criado para interagir de maneira contínua com a LLM
while True:
    looping = input("Se desejar fazer uma pergunta digite sim, porém se quiser sair digite qualquer coisa:\n")

    if looping != "sim":
        break
    else:
        rag_question = input("Gostaria de utilizar RAG? Se sim, digite 'sim', se não digite qualquer coisa: ")

        if rag_question == "sim":
            recovery = RagGenerate()
            question = "Fale sobre Crispr"        #input("Digite sua pergunta: ")
            persona = "Fale de maneira direta"      #input("Digite a persona: ")

            # Obter documentos relevantes do RAG
            relevant_docs = recovery.compair_vector(question)
            
            # Extrair apenas o texto dos documentos
            context_text = ""
            if 'documents' in relevant_docs and relevant_docs['documents']:
                for doc_list in relevant_docs['documents']:
                    for doc in doc_list:
                        context_text += f"{doc}\n\n"

            # Criar o prompt completo
            full_prompt = f"""{persona}
                Responda com base nos seguintes documentos:
                {context_text}
                Pergunta: {question}
                """

            try:
                response = model.generate_content(full_prompt)
                print("***\n" + response.text + "\n***")
                
            except Exception as e:
                print(f"Erro ao gerar resposta: {e}")
        
        else:
            response = model.generate_content("Fale de maneira direta sobre Crispr")
            print("***\n" + response.text + "\n***")
            
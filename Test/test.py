import fitz

#Parte do processo responsável por extrair o texto do PDF
class Test():
    def __init__(self):
        self.pdf_path = "files/Texto_Exemplo-1.pdf"
        self.pdf_file = fitz.open(self.pdf_path)
        self.chunk_size = 500
        self.overlap_size = 30

    #Extrai o texto do PDF, armazena em uma string e retorna o valor
    def extract_text(self):
        text = ""

        for page in self.pdf_file:
            text += page.get_text("text")

            text = text.replace("\n", " ")
            text = " ".join(text.split())
            
        return text
    
    def extract_text_and_token(self):
        tokens = []
        initial_point = 0
        count = 0
        text = ""

        for page in self.pdf_file:
            text += page.get_text("text")

            text = text.replace("\n", " ")
            text = " ".join(text.split())

        for i in text:
            if i in [" ", "."]:
                token = text[initial_point:count + 1]
                initial_point = count + 1
                tokens.append(token)
            count += 1

        return [text, tokens]
    
    def split_data_per_period(self):
        text = self.extract_text_and_token()[0]
        chunks = []
        initial_point = 0
        count = 0

        for i in text:
            if i == ".":
                chunk = text[initial_point:count + 1]
                initial_point = count + 1
                chunks.append(chunk)

            count += 1

        return chunks
            
    def split_static_data(self):
        text = self.extract_text_and_token()[0]
        chunks = []
        start = 0
        text_length = len(text)

        while start < text_length:
            end = min(start + self.chunk_size, text_length)
            chunk = text[start:end]
            chunks.append(chunk)
            
            if end >= text_length:
                break
                
            start += self.chunk_size - self.overlap_size
            
            if self.overlap_size >= self.chunk_size:
                start = end
        
        return chunks

    def split_dinamic_data(self):
        text = self.extract_text()
        overlap = ""
        count = 0
        overlap_size = 10
        index_letter = 0
        index_start = 0
        chunks = []
        index_overlap = 1

        while index_letter < len(text):

            if text[index_letter] == ".":
                chunk = text[index_start:index_letter + 1]
                index_start = index_letter + 2
                chunks.append(overlap + chunk)

                print(f"Chunk: {len(chunk)}\nValor: {chunk}")

                while count < overlap_size:
                    print(f"Contados: {index_overlap}")
                    if chunk[-index_overlap] in [" ", ","]:
                        count += 1
                    
                    if index_overlap == len(chunk):
                        break

                    index_overlap += 1

                overlap = chunk[-index_overlap + 1:]
                count = 1
                index_overlap = 0

            index_letter += 1

        return chunks

A = Test()

print(A.split_dinamic_data())

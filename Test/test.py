import fitz

#Parte do processo responsável por extrair o texto do PDF
class Test():
    def __init__(self):
        self.pdf_path = "files/Texto_Exemplo-1.pdf"
        self.pdf_file = fitz.open(self.pdf_path)
        self.chunk_size = 500
        self.overlap_size = 30
        self.token_chunk_size = 50
        self.token_overlap_size = 10

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

    def split_data_per_token(self):
        tokens = self.extract_text_and_token()[1]
        chunks = []
        phrase = ""
        overlap = ""
        count = 0
        count_aux = 0
        initial_state = 0
        
        #Implementar com While ou For, analisar em qual dos dois é possível implementar o overlap
        while initial_state < len(tokens):
            phrase += tokens[count]
            overlap += tokens[self.token_overlap_size-self.token_chunk_size]

            if count == self.token_chunk_size or count_aux == len(tokens):
                chunks.append(overlap + " " + phrase)
                count = 0
                phrase = ""

            count += 1

        for token in tokens:
            phrase += token
            count += 1
            count_aux += 1

            if token == tokens[-self.overlap_size]:
                overlap += token
                print(overlap)

            if count == self.token_chunk_size or count_aux == len(tokens):
                chunks.append(overlap + " " + phrase)
                count = 0
                phrase = ""
        
        return chunks

A = Test()

print(A.split_data_per_token()[:2])
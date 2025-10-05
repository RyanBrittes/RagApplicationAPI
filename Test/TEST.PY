import fitz

#Parte do processo responsável por extrair o texto do PDF
class Test():
    def __init__(self):
        self.pdf_path = "files/Texto_Completo_Extraido.pdf"
        self.pdf_file = fitz.open(self.pdf_path)
        self.string_pdf = ""
        self.chunk_size = 500
        self.overlap_size = 30


    #Extrai o texto do PDF, armazena em uma string e retorna o valor
    def extract_text(self):

        for page in self.pdf_file:
            self.string_pdf += page.get_text()
            
        return self.string_pdf
    
    def split_data_period(self):
        text = self.extract_text()
        chunks = []
        initial_point = 0

        for i in text:
            if i == ".":
                chunk = text[initial_point:len(i)]
                chunks.append(chunk)
                initial_point = len(i) + 1
        print(chunks)
            
    def split_data(self):
        text = self.extract_text()
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

A = Test()

#for i in A.split_data()[0:3]:
#    print(f"\nChunk: {i}")

A.split_data_period() #Refazer, ainda não funciona
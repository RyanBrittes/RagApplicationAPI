import fitz

#Parte do processo responsável por extrair o texto do PDF
class ExtractorPDF():
    def __init__(self):
        self.pdf_path = "files/Texto_Exemplo.pdf"
        self.pdf_file = fitz.open(self.pdf_path)
        self.string_pdf = ""

    #Extrai o texto do PDF, armazena em uma string e retorna o valor
    def extract_text(self):

        for page in self.pdf_file:
            self.string_pdf += page.get_text()
            
        return self.string_pdf
    
#A = ExtractorPDF()

#print(A.extract_text())
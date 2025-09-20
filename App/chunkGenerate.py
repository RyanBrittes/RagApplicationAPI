from extractorPDF import ExtractorPDF

class ChunkGenerate():
    def __init__(self):
        self.extractor = ExtractorPDF()
        self.chunk_size = 50
        self.overlap_size = 10

    def split_data(self):
        text = self.extractor.extract_text()
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
    

#A = ChunkGenerate()

#print(A.split_data())
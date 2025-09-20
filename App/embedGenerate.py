from chunkGenerate import ChunkGenerate
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

class EmbedGenerate():
    def __init__(self):
        self.chunks = ChunkGenerate()
        self.client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

    def embed_text(self, batch_size=32):
        texts = self.chunks.split_data()
        embeddings = []

        for i in range(0, len(texts), batch_size):
            batch = texts[i:i+batch_size]
            output = self.client.models.embed_content(
                model="gemini-embedding-001",
                contents=batch,
                config=types.EmbedContentConfig(output_dimensionality=128)
            ).embeddings
            embeddings.extend([emb.values for emb in output])

        return embeddings
    
    def embed_query(self, query: str):
        output = self.client.models.embed_content(
            model="gemini-embedding-001",
            contents=[query],
            config=types.EmbedContentConfig(output_dimensionality=128)
            ).embeddings
        
        return output[0].values

#A = EmbedGenerate()

#print(A.embed_text())
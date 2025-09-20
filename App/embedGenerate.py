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

    def embed_text(self):
        output = self.client.models.embed_content(
            model="gemini-embedding-001",
            contents=self.chunks.split_data(),
            config=types.EmbedContentConfig(output_dimensionality=128)
            ).embeddings
        return output[0].values
    
    def embed_query(self, query: str):
        output = self.client.models.embed_content(
            model="gemini-embedding-001",
            contents=query,
            config=types.EmbedContentConfig(output_dimensionality=128)
            ).embeddings
        return output[0].values

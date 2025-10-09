import chromadb
from chromadb.config import Settings
from Backend.embedGenerate import EmbedGenerate
from Backend.chunkGenerate import ChunkGenerate

#Classe que utiliza o ChromaDB como armazenamento vetorial
class VectorStore:
    def __init__(self):
        self.embedding = EmbedGenerate()
        self.documents = ChunkGenerate()
        self.client = chromadb.PersistentClient(
            path="ChromaDB",
            settings=Settings(allow_reset=True)
            )

    def collection_verify_create(self, collection_name):
        verify_collections = self.client.list_collections()
        collection_names = [col.name for col in verify_collections]
        if collection_name not in collection_names:
            self.client.create_collection(name=collection_name)
            print("Nova coleção criada")            
    
    #Método que adiciona os embeddings e documentos na coleção do ChromaDB
    def collection_add(self, collection_name):
        self.collection_verify_create(collection_name)

        collection = self.client.get_collection(name=collection_name)
        
        if collection.count() == 0:
            documents = self.documents.create_static_chunk()
            
            embeddings = self.embedding.embed_text()
            
            ids = [f"id{i}" for i in range(len(documents))]
            
            print(f"Documentos: {len(documents)}, Embeddings: {len(embeddings)}, IDs: {len(ids)}")
            
            if len(documents) == len(embeddings) == len(ids):
                collection.add(
                    embeddings=embeddings,
                    documents=documents,
                    ids=ids
                )
                print("Dados adicionados ao BD")
            else:
                raise ValueError(f"Tamanhos inconsistentes - Documentos: {len(documents)}, Embeddings: {len(embeddings)}, IDs: {len(ids)}")

    
    #Método que realiza a consulta na coleção do ChromaDB, trazendo os 3 resultados mais relevantes
    def collection_query(self, query, collection_name):
         self.collection_add(collection_name)

         collection = self.client.get_collection(name=collection_name)

         return collection.query(
            query_embeddings=query,
            n_results=10
        )

#Coleções criadas: [Chunk_Static_CH500_OV50, Chunk_Dinamic_O10]

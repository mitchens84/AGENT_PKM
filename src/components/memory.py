from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv 

load_dotenv(dotenv_path="config/.env")
class VectorStore:
    def __init__(self):
        self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.index_name = os.getenv("PINECONE_INDEX_NAME")
        self._ensure_index_exists()
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = PineconeVectorStore.from_existing_index(self.index_name, self.embeddings)

    def _ensure_index_exists(self):
        if self.index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=self.index_name,
                dimension=1536,
                metric='cosine',
                spec=ServerlessSpec(cloud='aws', region='us-west-2')
            )

    def similarity_search(self, query: str, k: int = 5) -> str:
        results = self.vector_store.similarity_search(query, k=k)
        response = "Found relevant information from your personal data:\n\n"
        for i, doc in enumerate(results, 1):
            source = doc.metadata.get('source', 'Unknown')
            response += f"{i}. {doc.page_content[:200]}...\n"
            response += f"   Source: Personal Data - {source}\n\n"
        return response.strip()

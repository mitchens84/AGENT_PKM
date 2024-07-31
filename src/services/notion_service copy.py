from langchain_community.document_loaders import NotionDBLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/.env")

def query_notion(query: str) -> str:
    loader = NotionDBLoader(
        integration_token=os.getenv("NOTION_INTEGRATION_TOKEN"),
        database_id=os.getenv("NOTION_DATABASE_ID")
    )
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    results = db.similarity_search(query, k=3)

    response = f"Source: Notion\nFound {len(results)} relevant documents related to: {query}\n\n"
    for i, doc in enumerate(results, 1):
        page_title = doc.metadata.get('title', 'Untitled')
        page_url = doc.metadata.get('url', 'No URL available')
        response += f"{i}. {doc.page_content[:200]}...\n"
        response += f"   Source: Notion - {page_title} ({page_url})\n\n"

    return response.strip()

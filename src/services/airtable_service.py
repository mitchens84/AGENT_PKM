from langchain_community.document_loaders import AirtableLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
from typing import Dict, List, Optional

load_dotenv(dotenv_path="config/.env")

def query_airtable(query: str, bases: Optional[Dict[str, List[str]]] = None) -> str:
    if bases is None:
        bases = {os.getenv("AIRTABLE_BASE_ID"): [os.getenv("AIRTABLE_TABLE_ID")]}

    all_docs = []
    for base_id, table_ids in bases.items():
        for table_id in table_ids:
            loader = AirtableLoader(
                api_token=os.getenv("AIRTABLE_API_KEY"),
                base_id=base_id,
                table_id=table_id
            )
            all_docs.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(all_docs)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    results = db.similarity_search(query, k=5)  # Increased to 5 for more comprehensive results

    response = f"Source: Airtable\nFound {len(results)} relevant records related to: {query}\n\n"
    for i, doc in enumerate(results, 1):
        record_id = doc.metadata.get('record_id', 'No ID available')
        base_id = doc.metadata.get('base_id', 'Unknown Base')
        table_id = doc.metadata.get('table_id', 'Unknown Table')
        response += f"{i}. {doc.page_content[:200]}...\n"
        response += f"   Source: Airtable - Base ID: {base_id}, Table ID: {table_id}, Record ID: {record_id}\n\n"

    return response.strip()
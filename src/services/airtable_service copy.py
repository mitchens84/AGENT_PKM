from langchain_community.document_loaders import AirtableLoader
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/.env")

def query_airtable(query: str) -> str:
    loader = AirtableLoader(
        api_token=os.getenv("AIRTABLE_API_KEY"),
        base_id=os.getenv("AIRTABLE_BASE_ID"),
        table_id=os.getenv("AIRTABLE_TABLE_ID")
    )
    docs = loader.load()
    
    relevant_docs = [doc for doc in docs if query.lower() in doc.page_content.lower()]
    
    response = f"Source: Airtable\nFound {len(relevant_docs)} relevant records related to: {query}\n\n"
    for i, doc in enumerate(relevant_docs, 1):
        record_id = doc.metadata.get('record_id', 'No ID available')
        response += f"{i}. {doc.page_content[:200]}...\n"
        response += f"   Source: Airtable - Record ID: {record_id}\n\n"
    
    return response.strip()

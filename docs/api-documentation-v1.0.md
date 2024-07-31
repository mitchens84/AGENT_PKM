# AGENT_PKM API Documentation

## Agents

### PKMAgent

The main agent responsible for processing queries and managing the research workflow.

#### Methods:
- `process_query(query: str) -> str`: Process a text query and return a response.
- `handle_voice(voice_file_path: str) -> str`: Process a voice message and return a response.
- `query_personal_data(query: str) -> str`: Query the personal vector store for relevant information.

## Components

### VectorStore

Manages the Pinecone vector store for efficient similarity search.

#### Methods:
- `similarity_search(query: str, k: int = 5) -> str`: Perform a similarity search and return formatted results.

## Services

### NotionService

#### Functions:
- `query_notion(query: str) -> str`: Query Notion database and return relevant information.

### AirtableService

#### Functions:
- `query_airtable(query: str) -> str`: Query Airtable and return relevant information.

## Utils

### DataUtils

#### Functions:
- `download_voice_message(file) -> str`: Download a voice message from Telegram.
- `transcribe_audio(file_path: str) -> str`: Transcribe an audio file to text.

## State

### StateManager

Manages the state of the research workflow.

#### Methods:
- `set_state(key: str, value: Any)`: Set a state value.
- `get_state(key: str) -> Any`: Get a state value.
- `clear_state()`: Clear all state values.

## Workflows

### ResearchWorkflow

Implements the research process workflow.

#### Methods:
- `run(inputs: dict) -> dict`: Run the complete research workflow and return results.

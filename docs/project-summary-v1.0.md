# AGENT_PKM SUMMARY

## Project Overview
AGENT_PKM is a Personal Knowledge Management (PKM) assistant implemented as a Telegram bot. It uses various AI tools and services to perform research tasks and answer user queries through both text and voice interactions.

## Key Components

1. **Telegram Bot Interface**: Handles user interactions through Telegram, supporting both text and voice messages.
2. **PKM Agent**: Manages the overall process of handling queries and generating responses.
3. **Research Workflow**: Implements a modular research and response generation workflow.
4. **Vector Store**: Uses Pinecone for efficient similarity search of embedded documents.
5. **Language Models**: Utilizes OpenAI's GPT models for analysis and response generation.
6. **External Data Sources**: Integrates with Notion, Airtable, and personal vector store for comprehensive research.
7. **Voice Transcription**: Uses AssemblyAI for transcribing voice messages to text.

## Main Workflow

1. **Receive Query**: Accept text or voice input from the user via Telegram.
2. **Process Query**: 
   - For text: Directly initiate the research process.
   - For voice: Transcribe the audio to text using AssemblyAI, then initiate the research process.
3. **Research**: Gather information from Notion, Airtable, and personal vector store.
4. **Analyze Results**: Synthesize gathered information using AI models.
5. **Generate Response**: Produce a final, structured response for the user.
6. **Send Response**: Deliver the response back to the user via Telegram.

## Key Files and Their Purposes

- `src/main.py`: Entry point for the Telegram bot, manages message handling and bot setup.
- `src/agents/pkm_agent.py`: Main PKM agent implementation, coordinates query processing.
- `src/components/memory.py`: Vector store management using Pinecone.
- `src/services/notion_service.py`: Notion integration for data retrieval.
- `src/services/airtable_service.py`: Airtable integration for data retrieval.
- `src/utils/data_utils.py`: Utility functions for data processing, including voice message handling and transcription.
- `src/state/state_manager.py`: Workflow state management.
- `src/workflows/research_workflow.py`: Research process implementation, orchestrates the entire query-response workflow.
- `config/config.py`: Configuration and environment variable management.
- `requirements.txt`: Python package dependencies.

## Recent Updates

1. Resolved circular import issues between PKMAgent and ResearchWorkflow.
2. Implemented asynchronous voice message handling and transcription using AssemblyAI.
3. Updated the main script to properly initialize and connect PKMAgent with ResearchWorkflow.
4. Improved error handling and logging throughout the application.

## Setup and Deployment

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up `.env` file with necessary API keys and configurations.
4. Run the bot: `python src/main.py`

## Current Features

1. Text and voice query processing
2. Integration with Notion, Airtable, and personal vector store
3. AI-powered analysis and response generation
4. Modular and extensible architecture
5. Asynchronous handling of voice messages

## Future Enhancements

1. Implement multi-modal capabilities (image processing)
2. Add a web interface in addition to the Telegram bot
3. Implement a feedback loop for continuous improvement of responses
4. Expand to additional data sources and knowledge bases
5. Implement fine-tuning of language models on domain-specific data
6. Enhance error handling and recovery mechanisms
7. Implement user authentication and multi-user support
8. Implement more sophisticated search algorithms (e.g., semantic search using embeddings)
9. Implement pre-processing of queries to extract key terms or intent
10. Implement post-processing of retrieved data to rank or filter results before sending them to the LLM

## Maintenance and Monitoring

- Use logging to track bot usage and errors
- Regularly update dependencies to ensure security and compatibility
- Monitor API usage to stay within quota limits
- Implement automated testing and continuous integration

For any questions or issues, please refer to the documentation or contact the project maintainers.

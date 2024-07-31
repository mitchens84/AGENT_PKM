# AGENT_PKM Configuration Guide

This guide explains how to set up the necessary environment variables and configurations for AGENT_PKM.

## Environment Variables

Create a `.env` file in the root directory of the project and add the following variables:

```
# Telegram Bot
TELEGRAM_BOT_TOKEN=your_telegram_bot_token

# OpenAI
OPENAI_API_KEY=your_openai_api_key

# Pinecone
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment

# Notion
NOTION_API_KEY=your_notion_api_key
NOTION_DATABASE_ID=your_notion_database_id

# Airtable
AIRTABLE_API_KEY=your_airtable_api_key
AIRTABLE_BASE_ID=your_airtable_base_id

# AssemblyAI
ASSEMBLYAI_API_KEY=your_assemblyai_api_key
```

Replace `your_*` with your actual API keys and configuration values.

## Configuration File

The `config/config.py` file contains additional configuration settings. Review and modify this file as needed for your specific setup.

## Setup Steps

1. Clone the repository
2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create the `.env` file as described above
5. Review and modify `config/config.py` if necessary
6. Run the application:
   ```
   python src/main.py
   ```

For any issues with configuration, please refer to the [Troubleshooting Guide](troubleshooting.md) or contact the project maintainers.
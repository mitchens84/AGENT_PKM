# AGENT_PKM Troubleshooting Guide

This guide addresses common issues you might encounter while setting up or running AGENT_PKM.

## 1. Environment Variables Not Loaded

**Issue**: The application fails to start due to missing environment variables.

**Solution**: 
- Ensure you've created a `.env` file in the root directory of the project.
- Check that all required variables are present in the `.env` file.
- Make sure you're running the application from the project root directory.

## 2. Dependency Installation Failures

**Issue**: `pip install -r requirements.txt` fails to install all dependencies.

**Solution**:
- Ensure you're using a compatible Python version (3.7+).
- Try updating pip: `pip install --upgrade pip`
- If a specific package fails, try installing it separately and check for any error messages.

## 3. Telegram Bot Not Responding

**Issue**: The Telegram bot is not responding to messages.

**Solution**:
- Verify that the `TELEGRAM_BOT_TOKEN` in your `.env` file is correct.
- Ensure the bot is running (`python src/main.py`).
- Check the console output for any error messages.

## 4. API Rate Limiting

**Issue**: You're encountering rate limit errors from external APIs (OpenAI, Pinecone, etc.).

**Solution**:
- Implement retry logic with exponential backoff.
- Consider upgrading your API plan if you're consistently hitting limits.

## 5. Memory Issues

**Issue**: The application crashes due to memory errors.

**Solution**:
- Review your vector store usage and consider optimizing large data operations.
- Ensure you're not storing unnecessary data in memory.

## 6. Slow Response Times

**Issue**: The bot takes a long time to respond to queries.

**Solution**:
- Review your `ResearchWorkflow` implementation for potential optimizations.
- Consider caching frequently accessed data.
- Check network latency to external APIs.

## 7. Incorrect or Irrelevant Responses

**Issue**: The bot provides incorrect or irrelevant information.

**Solution**:
- Review and refine your prompts for the language model.
- Check the data sources (Notion, Airtable, vector store) for accuracy.
- Consider fine-tuning the language model on domain-specific data.

If you encounter any issues not covered in this guide, please:

1. Check the application logs for error messages.
2. Review the [Configuration Guide](configuration.md) to ensure proper setup.
3. If the problem persists, contact the project maintainers with a detailed description of the issue, including any relevant logs or error messages.
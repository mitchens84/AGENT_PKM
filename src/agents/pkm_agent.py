import os
import sys
from dotenv import load_dotenv

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

load_dotenv(dotenv_path="config/.env")

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from src.utils.data_utils import download_voice_message, transcribe_audio
from src.agents.base_agent import BaseAgent

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class PKMAgent(BaseAgent):
    def __init__(self):
        # We'll initialize vector store functionality when needed
        self.workflow = None  # We'll set this later to avoid circular import

    def set_workflow(self, workflow):
        self.workflow = workflow

    def process_query(self, query: str) -> str:
        if self.workflow is None:
            raise ValueError("Workflow has not been set")
        inputs = {"query": query, "llm_choice": "gpt-4o-mini"}
        result = self.workflow.run(inputs)
        return result.get("response", "I'm sorry, but I couldn't generate a response to your query.")

    def handle_voice(self, voice_file_path: str) -> str:
        transcription = transcribe_audio(voice_file_path)
        return self.process_query(transcription)

    def query_personal_data(self, query: str) -> str:
        # Implement this method based on your actual vector store implementation
        # For now, we'll return a placeholder message
        return "Vector store query not implemented yet."
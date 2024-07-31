import os
from dotenv import load_dotenv
import asyncio
import aiohttp
import assemblyai as aai
import logging

load_dotenv(dotenv_path="config/.env")

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def download_voice_message(file):
    try:
        voice_file = await file.get_file()
        file_path = f"temp_voice_{file.file_unique_id}.ogg"
        await voice_file.download_to_drive(file_path)
        return file_path
    except Exception as e:
        logger.error(f"Error downloading voice message: {str(e)}")
        raise

async def transcribe_audio(file_path: str) -> str:
    try:
        config = aai.TranscriptionConfig(language_code="en")
        
        transcriber = aai.Transcriber()
        
        # Use run_in_executor to run the synchronous method in a separate thread
        loop = asyncio.get_event_loop()
        transcript = await loop.run_in_executor(None, transcriber.transcribe, file_path, config)
        
        if transcript.status == aai.TranscriptStatus.error:
            logger.error(f"Transcription error: {transcript.error}")
            raise Exception(f"Transcription failed: {transcript.error}")
        
        return transcript.text
    except Exception as e:
        logger.error(f"Error transcribing audio: {str(e)}")
        raise
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)  # Clean up the temporary file
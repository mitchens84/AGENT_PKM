from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    def process_query(self, query: str) -> str:
        pass

    @abstractmethod
    def handle_voice(self, voice_file_path: str) -> str:
        pass

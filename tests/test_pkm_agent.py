import sys
sys.path.insert(0,'/Users/mitchens/Local/6I-CYBORG-AGENTS/AGENT_PKM')

import pytest
from unittest.mock import Mock, patch
from src.agents.pkm_agent import PKMAgent
from src.workflows.research_workflow import ResearchWorkflow

@pytest.fixture
def pkm_agent():
    with patch('src.agents.pkm_agent.VectorStore') as mock_vector_store:
        mock_vector_store.return_value.similarity_search.return_value = "Found relevant information from your personal data:"
        agent = PKMAgent()
        workflow = ResearchWorkflow()
        agent.set_workflow(workflow)
        yield agent

def test_process_query(pkm_agent):
    with patch.object(pkm_agent.workflow, 'run') as mock_run:
        mock_run.return_value = {"response": "Test response"}
        result = pkm_agent.process_query("Test query")
        assert result == "Test response"

def test_handle_voice(pkm_agent):
    with patch('src.agents.pkm_agent.transcribe_audio') as mock_transcribe:
        with patch.object(pkm_agent.workflow, 'run') as mock_run:
            mock_transcribe.return_value = "Transcribed text"
            mock_run.return_value = {"response": "Test response"}
            result = pkm_agent.handle_voice("test_audio.ogg")
            assert result == "Test response"
            mock_transcribe.assert_called_once_with("test_audio.ogg")

def test_query_personal_data(pkm_agent):
    result = pkm_agent.query_personal_data("Test query")
    assert result == "Found relevant information from your personal data:"
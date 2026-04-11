import os

from dotenv import load_dotenv
from pathlib import Path


env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)



# --- project file import to into ---
from graph.graph import app
from ingestion import retriever



def test_retriever_is_working():
    """Check if any documents have been returned from the database."""
    question = "RAG nedir?"

    docs = retriever.invoke(question)

    assert isinstance(docs, list)
    if len(docs) > 0:
        assert hasattr(docs[0], "page_content")


def test_router_decision_logic():
    """IMPORTANT : This tests whether the router is routing to the correct node."""
    inputs = {"question": "Fransa'nın başkenti neresidir?"}

    # LangGraph invoke tests
    result = app.invoke(inputs)

    assert "generation" in result
    assert isinstance(result["generation"], str)



from dotenv import load_dotenv
from pathlib import Path

# 1. .env load
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def test_generate_node_mocked(mocker):
    """IMPORTANT : It tests the Generation node without making an actual OpenAI call."""

    # 2. first mock
    mock_llm = mocker.patch("langchain_openai.ChatOpenAI.invoke")

    from langchain_core.messages import AIMessage
    mock_llm.return_value = AIMessage(content="Bu bir mock cevaptır.")

    # 3. import
    from graph.nodes.generate import generate

    sample_state = {
        "question": "Test sorusu",
        "documents": ["Test dökümanı içeriği"]
    }

    # run
    result = generate(sample_state)

    # check result
    assert result["generation"] == "Bu bir mock cevaptır."
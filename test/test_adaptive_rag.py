import os
import pytest
from dotenv import load_dotenv
from pathlib import Path

# --- KRİTİK SIRALAMA: Importlardan ÖNCE anahtarı yükle ---
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Eğer hala hata alıyorsan, manuel olarak buraya ata (Sadece test için)
if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = "sk-proj-senin-anahtarin"

# --- ŞİMDİ PROJE DOSYALARINI İÇE AKTARABİLİRİZ ---
from graph.graph import app
from ingestion import retriever
from langchain_core.messages import AIMessage


def test_retriever_is_working():
    """Vektör veritabanından belge dönüp dönmediğini test eder."""
    question = "RAG nedir?"
    # LangChain 0.3 standartı: invoke kullanılır
    docs = retriever.invoke(question)

    assert isinstance(docs, list)
    if len(docs) > 0:
        assert hasattr(docs[0], "page_content")


def test_router_decision_logic():
    """Router'ın doğru düğüme yönlendirme yapıp yapmadığını test eder."""
    inputs = {"question": "Fransa'nın başkenti neresidir?"}

    # LangGraph invoke testi
    result = app.invoke(inputs)

    assert "generation" in result
    assert isinstance(result["generation"], str)


import os
import pytest
from dotenv import load_dotenv
from pathlib import Path

# 1. .env yükle
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def test_generate_node_mocked(mocker):
    """Generation düğümünü gerçek OpenAI çağrısı yapmadan test eder."""

    # 2. ÖNCE MOCKLA: ChatOpenAI daha oluşmadan biz onun yolunu kesiyoruz
    mock_llm = mocker.patch("langchain_openai.ChatOpenAI.invoke")

    from langchain_core.messages import AIMessage
    mock_llm.return_value = AIMessage(content="Bu bir mock cevaptır.")

    # 3. ŞİMDİ IMPORT ET: Fonksiyonun içinde import ederek erken patlamayı önlüyoruz
    from graph.nodes.generate import generate

    sample_state = {
        "question": "Test sorusu",
        "documents": ["Test dökümanı içeriği"]
    }

    # Çalıştır
    result = generate(sample_state)

    # Kontrol et
    assert result["generation"] == "Bu bir mock cevaptır."
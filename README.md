# What's AdaptiveRAG Project
Welcome to Adaptive-RAG, a sophisticated implementation of Retrieval-Augmented Generation that intelligently adapts its retrieval strategy based on the complexity of the user's query.

## 🚀 Adaptive-RAG: Dynamic Strategy Selection for RAG Systems
Standard RAG systems often treat every query with the same retrieval logic, which can lead to inefficiency for simple questions or insufficient context for complex ones. This project implements an adaptive layer that classifies incoming queries and routes them through the most effective pipeline:

- No Retrieval: For direct or subjective questions where the LLM's internal knowledge suffices.
- Single-Step RAG: For straightforward factual queries requiring specific external data.
- Multi-Step/Iterative RAG: For complex, multi-hop reasoning tasks that require gathering information from multiple sources.

## ✨ Key Features
- Intelligent Query Router: Dynamically analyzes query complexity to save latency and tokens.
- Multi-Step Reasoning: Capable of breaking down complex prompts into sub-queries.
- Self-Correction Mechanism: Evaluates the relevance of retrieved documents before generating the final answer.
- Modular Architecture: Easily swap out LLMs (OpenAI, Anthropic, Llama) or Vector Databases (Pinecone, Chroma, FAISS).

## 🛠️ Tech Stack
- Framework: LangChain / Langgraph
- LLMs Model: gpt-5 
- Vector Store: ChromaDB
- Language: Python 3.x
- Trace: Langsmith
- User Interface: Streamlit

## 🎨 User Interface
The project includes a user-friendly web interface built with Streamlit, allowing users to interact with the Adaptive-RAG system in real-time.

- Interactive Chat Interface: Seamlessly ask questions and view the RAG's reasoning process.
- Strategy Visualization: The UI displays which retrieval strategy (No Retrieval, Single-Step, or Multi-Step) was chosen for your specific query.
- Traceability: View the retrieved document chunks and confidence scores directly in the sidebar.



## 📖 Documentation

- https://docs.langchain.com/oss/python/langgraph/overview – Comprehensive documentation, including conceptual overviews and guides
- https://github.com/langchain-ai/langgraph - For langgraph framework usage and details


## 🖥️ Installation
1) Clone the repository:

```bash
Bash
git clone https://github.com/mehmetalikoker/adaptive-rag.git
```

2) Set up your environment variables in a .env file:
```bash
- OPENAI_API_KEY
- LANGCHAIN_API_KEY
- LANGCHAIN_TRACING_V2 Info
- LANGCHAIN_PROJECT Info
- TAVILY_API_KEY
```



## 🖥️ How It Works
Running the class via terminal is sufficient.

 ```bash
For the UI version 
- Terminal -> streamlit run app.py
 ```

## 🎨 How Does It Look

<img width="1392" height="906" alt="Ekran görüntüsü 2026-04-05 180811" src="https://github.com/user-attachments/assets/81159018-598b-4180-95d6-cc124bac8078" />


## 🎨 Execution Flow & Backend Logs
To understand how the Adaptive Router makes decisions and how the iterative retrieval process works, you can monitor the backend logs in your terminal.

<img width="1304" height="422" alt="Ekran görüntüsü 2026-04-06 100739" src="https://github.com/user-attachments/assets/05d223ba-e46e-4a7b-993d-4c7611fc39cc" />

# 🦜 LangChain – Day 12: Ollama

Day 12 was short but important — running an LLM **completely locally** using Ollama, with zero API keys and zero cloud dependency.

---

## 🖥️ What is Ollama?
Ollama lets you download and run open-source LLMs directly on your machine. Combined with `langchain_ollama`, it plugs straight into any existing LangChain chain with the same `.invoke()` interface — swap out `ChatOpenAI` for `ChatOllama` and everything else just works.

## 🦙 Running Llama 3.2 Locally
Used `ChatOllama` with `llama3.2:1b` — a lightweight 1B parameter model that runs on CPU without needing a GPU. One line to load, one line to invoke.

## 💡 Why It Matters
Everything built so far — chains, RAG pipelines, agents — can now run fully offline. No API costs, no rate limits, no data leaving your machine. For local prototyping and privacy-sensitive use cases, this is a big deal.

---

*Stack: LangChain · Ollama · Llama 3.2*
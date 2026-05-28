from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
# 🦜 LangChain – Day 01: Models

First day diving into LangChain — explored the three core model types: **LLMs, Chat Models, and Embedding Models**. Tried multiple providers (OpenAI + HuggingFace) and built a small semantic search at the end.

---

## 🤖 LLMs
Used LangChain's `OpenAI` wrapper with `gpt-3.5-turbo-instruct` to send a plain text prompt and get a raw completion back. Simple input → output, no conversation context.

## 💬 Chat Models
Chat models are smarter and conversation-aware. Tried three different ways to use them:
- **OpenAI** — `gpt-4o-mini` via `ChatOpenAI`, cleanest and simplest.
- **HuggingFace API** — ran `Llama 3.1 8B Instruct` remotely using a HuggingFace token.
- **HuggingFace Local** — loaded `TinyLlama` directly on machine using a pipeline (needs GPU/PyTorch setup).

All three share the same `.invoke()` interface — that's the beauty of LangChain's abstraction.

## 🔢 Embedding Models
Embeddings turn text into vectors (lists of numbers) that capture **meaning**. Learned two providers:
- **OpenAI** — `text-embedding-3-small`, used both `embed_query()` for a single string and `embed_documents()` for a list.
- **HuggingFace** — `sentence-transformers/all-MiniLM-L6-v2` as a free alternative.

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=250,
    chunk_overlap=0,
)

result = splitter.split_text(text)

print(len(result))
print(result)

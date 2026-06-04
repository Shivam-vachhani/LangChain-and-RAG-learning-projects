# 🦜 LangChain – Day 08: Vector Stores

Day 8 was about **storing and searching embeddings** — the core infrastructure behind any RAG system. Explored two vector stores: Chroma (local) and Pinecone (cloud).

---

## 🗄️ What is a Vector Store?

After splitting and embedding documents, you need somewhere to store and search those vectors efficiently. A vector store handles that — you store embedded documents once, then query semantically at any time.

## 🟣 Chroma (Local)

Used `Chroma` as a local vector store with a persistent directory (`./chroma_db`). Practiced the full CRUD lifecycle on a set of IPL player documents:

- **Add** — embedded and stored 5 player docs with team metadata.
- **View** — fetched stored documents with their embeddings and metadata.
- **Delete** — removed documents by ID.
- **Update** — replaced a document with an updated version using `update_document()`.
- **Search** — ran `similarity_search()` to find relevant docs for a query, `similarity_search_with_score()` to get distances, and **metadata filtering** to restrict results to a specific team (e.g. only Chennai Super Kings players).

## 🌲 Pinecone (Cloud)

Repeated the same workflow with `PineconeVectorStore` — a managed cloud vector DB. The interface is nearly identical to Chroma, which shows how LangChain abstracts the underlying store. Key difference: Pinecone doesn't have a native `update_document()`, so updates are done by re-adding with the same ID via `add_documents()`.

## 🔑 Key Concepts Practiced

- `similarity_search(query, k=2)` — top-k semantic search
- `similarity_search_with_score()` — same but returns distance scores
- Metadata filtering — narrowing search results by field values
- Persistence — Chroma saves to disk, Pinecone saves to cloud index

---

_Stack: LangChain · Chroma · Pinecone · OpenAI Embeddings_

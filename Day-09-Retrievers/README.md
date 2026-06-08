# 🦜 LangChain – Day 09: Retrievers

Day 9 was about **retrievers** — the layer that sits between a vector store and the LLM, responsible for fetching the right documents for a given query. Explored 4 different retrieval strategies.

---

## 🔍 VectorStore Retriever (Baseline)
The simplest retriever — just calls `.as_retriever()` on a Pinecone vector store and does a plain similarity search. Returns the top-k most similar documents. This is the default starting point for any RAG pipeline.

## ⚖️ MMR Retriever (Maximal Marginal Relevance)
Problem with plain similarity search: if multiple documents say the same thing, you get redundant results. MMR fixes this by balancing **relevance** and **diversity** — `lambda_mult` controls the tradeoff (lower = more diverse). Tested it on 3 nearly identical Virat Kohli century reports — MMR avoids returning all three duplicates and picks a more varied result set.

## 🔀 Multi-Query Retriever (Manual)
Plain similarity search is limited by the exact wording of the query. Built a custom multi-query retriever that uses an LLM to **rephrase the original question into 3 different versions**, runs each against the vector store, then deduplicates the combined results. Compared it side-by-side against simple similarity — multi-query consistently surfaces more relevant docs that the original query would have missed.

## 🌐 Wikipedia Retriever
Not everything needs to be in your own vector store. `WikipediaRetriever` fetches live documents directly from Wikipedia for a query — no embedding or indexing needed. Used it to pull articles comparing Nioh and Nioh 2.

---

*Stack: LangChain · Pinecone · OpenAI · Wikipedia*
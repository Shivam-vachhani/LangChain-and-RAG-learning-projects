# 🦜 LangChain – Day 10: Basic RAG

Day 10 was the first full **RAG (Retrieval-Augmented Generation) pipeline** — everything from Day 1 to Day 9 came together in a single project. Built a chatbot that answers questions about any YouTube video using its transcript.

---

## 🎬 Project — YouTube Q&A Chatbot

Ask any question about a YouTube video and get an answer grounded in the actual transcript — no hallucination, no guessing.

---

## 🔄 The RAG Pipeline (Step by Step)

**1. Indexing**

- Fetched the YouTube transcript using `YouTubeTranscriptApi`, handling edge cases like disabled captions or missing English subtitles.
- Split the transcript into chunks with `RecursiveCharacterTextSplitter` (`chunk_size=1000`, `chunk_overlap=200`) so context isn't lost at chunk boundaries.
- Embedded the chunks using `OpenAIEmbeddings` and stored them in a **Chroma** vector store.

**2. Retrieval**

- Converted the vector store into a retriever (`similarity`, `k=3`) to fetch the 3 most relevant chunks for any question.

**3. Augmentation**

- Formatted the retrieved chunks into a single context string using a `RunnableLambda`, then injected it into a `PromptTemplate` alongside the user's question.
- The prompt explicitly instructs the model not to hallucinate — if the context doesn't have the answer, say so.

**4. Generation**

- `ChatOpenAI` generates the final answer, `StrOutputParser` cleans it up.
- Wired everything together using `RunnableParallel` + `RunnablePassthrough` so context retrieval and question passing happen in one clean chain.

---

## 💡 Key Insight

RAG is just a pipeline — fetch → format → prompt → generate. Every piece was already learned in previous days; Day 10 was about connecting them all end-to-end for the first time.

---

_Stack: LangChain · OpenAI · Chroma · YouTubeTranscriptApi_

# 🦜 LangChain – Day 07: Text Splitters

Second week into LangChain — focused entirely on **Text Splitters**. Learned how to break large documents into smaller chunks before passing them to LLMs or storing in vector databases. Tried 5 different splitting strategies, from dumb character cuts to smart semantic chunking.

---

## 📏 Length-Based Splitting

Used `CharacterTextSplitter` to split a PDF (loaded via `PyPDFLoader`) by raw character count — `chunk_size=100` with `chunk_overlap=20`. Simple and fast, but doesn't care about sentence or word boundaries. Good starting point to understand how chunking works.

## 🧱 Structure-Based Splitting

Used `RecursiveCharacterTextSplitter` — LangChain's go-to general splitter. It tries paragraph breaks first, then line breaks, then sentences — only cutting mid-word as a last resort. Much cleaner chunks than pure length splitting.

## 📝 Markdown-Aware Splitting

Used `RecursiveCharacterTextSplitter.from_language(Language.MARKDOWN)` on a LangChain notes file. It respects Markdown syntax — keeps headings, sections, and blocks intact instead of slicing through them.

## 🐍 Python Code Splitting

Same `from_language()` approach but with `Language.PYTHON`. Splits source code while respecting class and function boundaries — so a method doesn't get cut in half across two chunks.

## 🧠 Semantic Meaning Splitting

The most interesting one — `SemanticChunker` from `langchain_experimental` backed by `OpenAIEmbeddings`. It embeds each sentence and splits only where the **meaning shifts significantly**, using percentile-based cosine distance. Tested on a passage mixing farming, IPL, and terrorism — it correctly identified 3 separate topic chunks with zero manual configuration.

---

_Stack: LangChain · LangChain Experimental · OpenAI Embeddings · PyPDFLoader_

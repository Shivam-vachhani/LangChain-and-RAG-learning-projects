# 🦜 LangChain – Day 06: Document Loaders

Day 6 was about **getting data into LangChain** — loading documents from different sources so they can later be processed, embedded, or fed into a RAG pipeline.

---

## 📄 Text File (Manual)
Loaded a `.txt` file using plain Python, then manually wrapped the content in a `Document` object with `page_content` and `metadata`. This is the most barebones approach — useful when you need full control over how a document is constructed.

## 📊 CSV Loader
Used `CSVLoader` to load a CSV file — each row becomes its own `Document`, which makes it easy to search or query individual records later.

## 📚 PDF Loader (Unstructured)
Loaded a PDF using `UnstructuredLoader` with a `fast` strategy and `basic` chunking — it automatically splits the PDF into chunks as `Document` objects. Useful for large PDFs where you don't want one giant blob of text.

## 📁 Directory Loader
Used `DirectoryLoader` to load **all PDFs in a folder** at once by pointing it at a directory, setting a `glob` pattern (`*.pdf`), and passing `PyPDFLoader` as the loader class. Scales up document ingestion without looping manually.

## 🌐 Web Loader
Loaded a live webpage using `WebBaseLoader` by passing a URL — it scrapes the HTML and wraps the content as a `Document`. Tested it on the Day 01 GitHub repo page itself.

---

*Stack: LangChain · langchain-community · langchain-unstructured*
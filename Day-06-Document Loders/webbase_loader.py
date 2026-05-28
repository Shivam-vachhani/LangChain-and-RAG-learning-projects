from langchain_community.document_loaders import WebBaseLoader

url='https://github.com/Shivam-vachhani/LangChain-and-RAG-learning-projects/tree/main/Day-01-Models'
loader= WebBaseLoader(url)

docs =loader.load()

print(docs)
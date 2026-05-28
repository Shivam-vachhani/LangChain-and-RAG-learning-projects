from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader('../Day-06-Document Loders/dl-curriculum.pdf')

docs = loader.load()

text = """ 
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.
These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=''
)

# split_texts = splitter.split_text(text)

split_texts = splitter.split_documents(docs)

print(split_texts[0].page_content)
from pathlib import Path
from langchain_core.documents import Document

file_path = Path('poem.txt')

with open(file_path,'r',encoding='utf-8') as f:
    file_content = f.read()

docs = [Document(page_content=file_content,metadata={"source":str(file_path)})]

print(docs)
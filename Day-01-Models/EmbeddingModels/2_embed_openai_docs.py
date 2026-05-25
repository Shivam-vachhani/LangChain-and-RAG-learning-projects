from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)

docs = [
    "Noih is Soulslike game by team ninja",
    "This game is famous for its smooth and fast combat style",
    "This game offers many missions and boss fights to engage gamers."
]

result = model.embed_documents(docs)

print(result)
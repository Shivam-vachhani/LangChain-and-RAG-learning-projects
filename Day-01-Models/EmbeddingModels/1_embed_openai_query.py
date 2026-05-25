from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)

result = model.embed_query("The Seven Wonders of the Modern World")

print(result)


from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

result = model.embed_query("with great power comes great responsibility")
# insted of model.embed_query we can use model.embed_documents for passing documents here 
print(result)

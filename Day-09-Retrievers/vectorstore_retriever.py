from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings()

vector_store = PineconeVectorStore(
    embedding=embedding_model,
    index_name='trial-index'
)

query = 'who is bowler?'

retriver=vector_store.as_retriever(search_kwargs={"k":2})

result = retriver.invoke(query)

print(result)
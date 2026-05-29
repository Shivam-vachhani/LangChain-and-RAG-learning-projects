from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

all_docs = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
]

embedding_model = OpenAIEmbeddings()
multiquery_model = ChatOpenAI(model='gpt-4o-mini')

vectorstore = PineconeVectorStore(
    embedding=embedding_model,
    index_name='trial-index'
)

vectorstore.add_documents(all_docs)

simple_retriver = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={'k':5}
)

template1 = PromptTemplate(
    template=(
    "You are an AI language model assistant. Your task is to generate 3 "
    "different versions of the given user question to retrieve relevant documents from a vector database.\n"
    "By generating multiple perspectives on the user question, your goal is to help "
    "the user overcome some of the limitations of distance-based similarity search.\n"
    "Provide these alternative questions separated by newlines.\n"
    "Original question: {question}"),
    input_variables=['question']
)

parser = StrOutputParser()

query = "How to improve energy levels and maintain balance?"

chain = template1  | multiquery_model | parser 

similarity_results = simple_retriver.invoke(query)

llm_result = chain.invoke({'question': query })

question_list = [q.strip() for q in llm_result.split('\n') if q.strip()]

multiquery_result = []
for q in question_list:
    docs = simple_retriver.invoke(q)
    multiquery_result.extend(docs)

multiquery_result =list({doc.page_content:doc for doc in multiquery_result}.values())

for i, doc in enumerate(similarity_results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

print("*"*150)

for i, doc in enumerate(multiquery_result):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
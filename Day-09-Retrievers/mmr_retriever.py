from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv 
from langchain_core.documents import Document

load_dotenv()

documents = [
    Document(
        page_content="Virat Kohli scored a brilliant century of 112 runs against Australia, leading India to a thrilling victory.",
        metadata={"source": "match_report_1"}
    ),
    Document(
        page_content="India won the match against Australia thanks to Virat Kohli's incredible 112-run hundred in the run chase.",
        metadata={"source": "match_report_2"}
    ),
    Document(
        page_content="A masterclass century (112 runs) by Virat Kohli secured a dramatic win for team India over Australia.",
        metadata={"source": "match_report_3"}
    ),
    Document(
        page_content="MS Dhoni announced his retirement from all forms of international cricket, ending an iconic era.",
        metadata={"source": "news_flash"}
    ),
    Document(
        page_content="The stadium pitch conditions were highly favorable for spin bowlers, showing deep cracks by day three.",
        metadata={"source": "pitch_analysis"}
    )
]

embedding_model = OpenAIEmbeddings()

vector_store = PineconeVectorStore(
    embedding=embedding_model,
    index_name='trial-index'
)

# vector_store.add_documents(documents)

retriver = vector_store.as_retriever(
    search_type='mmr',
    search_kwargs={"k":3,'lambda_mult':0.4}
)

query = 'Tell me about of virat kohli'

result = retriver.invoke(query)

for i , doc in enumerate(result):
    print(f'\n-------result{i+1}-------')
    print(f'Content : {doc.page_content}\n')


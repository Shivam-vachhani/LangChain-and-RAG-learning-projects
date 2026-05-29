from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled,NoTranscriptFound
from youtube_transcript_api.formatters import TextFormatter
from langchain_chroma import Chroma
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# Step 1a - indexing(Document Ingetion) 
video_id='wjZofJX0v4M'

try:
    ytt_api = YouTubeTranscriptApi() 
    transcript_list = ytt_api.fetch(video_id,languages=['en'])
    text_formatter = TextFormatter()
    transcript = text_formatter.format_transcript(transcript_list)
except TranscriptsDisabled:
    print("Caption are Disables for this Video")
except NoTranscriptFound:
    print("English language captions not found on this video")
except Exception as e:
    print(f'AN unexpected error occurred : {e}')


#  Step 1b - indexing(Text Splitting)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=splitter.split_text(transcript)


# Step 1c & 1d - indexing(Embeddings Creation & Vector Store Creation)
embeddings_model = OpenAIEmbeddings()
vector_store = Chroma.from_texts(chunks,embeddings_model)


# Step 2 - Retrival
retriver = vector_store.as_retriever(
    search_type='similarity',
    search_kwargs={'k':3}
)


# Step 3 - Augmentation
template = PromptTemplate(
    template =( """ you are a helpful Q&A assistant
    answer only from provided youtube transcript context.
    If the context is insufficient,just say you don't know.
    do not hullusiate on somthing not provided on context just say you don't know.
    Context : {context} \n 
    Question : {question}  
    """),
    input_variables=['context','question']
)

# Step 4 - Generation

model = ChatOpenAI(model='gpt-4o-mini')
parser= StrOutputParser()


# Building RAG pipeline 

def format_docs(retrived_docs):
    context = '\n\n'.join(docs.page_content for docs in retrived_docs)
    return context

# retrived_docs = retriver.invoke(question)
# print(format_docs(retrived_docs))

parallel_chain = RunnableParallel({
    'context': retriver | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

final_chain = parallel_chain | template | model | parser

question = 'what is softmax and how it works?'

result = final_chain.invoke(question)

print(result)
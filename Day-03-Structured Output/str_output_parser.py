from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task="text-gentration"
)

model=ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template='Give me report on topic : {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='give me sort summery on this text\n {text}',
    input_variables=['text']
)

#### without chains 
# prompt = template1.invoke({'topic':'balckhole'})
# result1 = model.invoke(prompt)
# prompt_final= template2.invoke({'text':result1.content})
# final_result = model.invoke(prompt_final)
#print(final_result.content)


#### With chains 
parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser 

final_result = chain.invoke({
    'topic':'nioh game'
})


print(final_result)
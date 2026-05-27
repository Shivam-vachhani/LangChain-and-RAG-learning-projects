from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch,RunnableSequence,RunnablePassthrough
from dotenv import load_dotenv 

load_dotenv()

model= ChatOpenAI(model='gpt-4o-mini')

parser = StrOutputParser()

template1= PromptTemplate(
    template='give me a sort report on {topic} less than 400 words',
    input_variables=['topic']
)

tempalte2= PromptTemplate(
    template='summerize the given report\n {report}',
    input_variables=['report']
)

base_chain=RunnableSequence(template1,model,parser)

parallel_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500 ,RunnableSequence(tempalte2 | model | parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(base_chain,parallel_chain)

result  = final_chain.invoke({'topic' : 'black hole'})

print(result)
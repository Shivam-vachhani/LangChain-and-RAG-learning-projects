from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence
from dotenv import load_dotenv 

load_dotenv()

model =ChatOpenAI(model='gpt-4o-mini')

template1 = PromptTemplate(
    template=('create sort guide for given game {game}'),
    input_variables=['game']
)

template2 = PromptTemplate(
    template=('give sort review of given game \n {game}'),
    input_variables=['game']
)

parser = StrOutputParser()

chain = RunnableParallel({
    'guide':RunnableSequence(template1,model,parser),
    'review':RunnableSequence(template2,model,parser)
})

result = chain.invoke({'game':'nioh'})

print(""" Review \n {} \n\n guide \n {}' """.format(result['review'],result['guide']))



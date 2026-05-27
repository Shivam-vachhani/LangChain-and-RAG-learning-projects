from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnableLambda,RunnablePassthrough
from dotenv import load_dotenv 

load_dotenv()

model= ChatOpenAI(model='gpt-4o-mini')

parser = StrOutputParser()

template1 = PromptTemplate(
    template='give me a joke on {topic}',
    input_variables=['template']
)

template2 = PromptTemplate(
    template='expalin given joke \n {joke}',
    input_variables=['joke']
)

def word_count(text):
    return len(text.split())

base_chain = RunnableSequence(template1 , model , parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(template2,model,parser),
    'word count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(base_chain,parallel_chain)

result = final_chain.invoke({'topic':'video games'})

print(""" ___________ Joke  ___________ \n {} \n\n\n___________ Joke explanation ___________  \n  {}  \n\n\n  ___________ WORDS___________\n {}""".format(result['joke'],result['explanation'],result['word count']))
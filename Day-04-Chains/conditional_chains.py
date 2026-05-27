from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

template1 = PromptTemplate(
    template=('Classify the given feedback either positive or nagative \n {feedback}'),
    input_variables=['feedback']
)

class Analysis(BaseModel):

    sentiment: Literal['positive','negative'] = Field(description="calssify feedback sentiment in either positive or nagative")

structured_model = model.with_structured_output(Analysis)
 

parserStr = StrOutputParser()

base_chain = template1 | structured_model

template2 = PromptTemplate(
    template=('give message according to given postive feedback \n {feedback}'),
    input_variables=['feedback']
)

template3 = PromptTemplate(
    template=('give message according to given negative feedback \n {feedback}'),
    input_variables=['feedback']
)

condition_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', template2 | model | parserStr),
    (lambda x:x.sentiment == 'negative', template3 | model | parserStr),
    RunnableLambda(lambda x: "Could not found any sentiment")
)

final_chain = base_chain | condition_chain 

result = final_chain.invoke({'feedback':'this is bestphone phonei ever buyed'})

print(result)

# final_chain.get_graph().print_ascii()
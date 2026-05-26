from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from dotenv import load_dotenv

load_dotenv()

class Person(BaseModel):
    name: str = Field(description="write down person name")
    age: int = Field(gt=18,description="Write down person's age")
    city: str = Field(description="write name of city that preson live")

#### outdated code

# llm=HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.1-8B-Instruct",
#     task='text-generation'
# )

# model=ChatHuggingFace(llm=llm)

# parser = PydanticOutputParser(pydantic_object=Person)
# template = PromptTemplate(
#     template="give fictional  person's name age and city from {place} \n {format_instructions}",
#     input_variables=['palce'],
#     partial_variables={'format_instructions': parser.get_format_instructions()}
# )


#### Industry practice 
model = ChatOpenAI(model='gpt-4o-mini',temperature=1.5)

structured_model= model.with_structured_output(Person)

template = ChatPromptTemplate([
    ('system','use are a helpful assistant that help to genrate frictional persons details'),
    ('human',"generate person's name age and city from {place}")
])

chain = template | structured_model 

final_result = chain.invoke({'place':'Japan'})

print(final_result)
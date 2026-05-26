from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field
load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

##### Using json schema good for croos language paltforms to send data from frontend to backend same formate
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

##### Using Pydantic library good for data validation for python language  
# class Review(BaseModel):
#     key_themes: list[str] = Field(description ='give list of key themes based of reivew')
#     summery:str = Field(description ='give sort summery in 1 line')
#     sentiment:Literal["good","bad"] = Field(description="assign semtimen according review")
#     pros:Optional[list[str]] = Field(default=None, description="write list of pros if review explicitly has pros else not write at all")
#     cons:Optional[list[str]] = Field(default=None, description="write list of cons if review explicitly has cons else not write at all")
#     reviewer:str = Field(description="write the reviewer name if exist else not write at all")

##### Using Typeddict not goog for type validation 
# class Review(TypedDict):
#     key_themes:Annotated[list[str],'give list of key themes based of reivew']
#     summery: Annotated[str,"give sort summery in 1 line"]
#     sentiment:Annotated[Literal['good','bad'],"assign semtimen according review"]
#     pros:Annotated[Optional[list[str]],"write list of pros if review explicitly has pros else not write at all"]
#     cons:Annotated[Optional[list[str]],"write list of cons if review explicitly has cons else not write any thing"]
#     reviewer:Annotated[Optional[str],"write the reviewer name if exist else not write at all"]


structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""While the battery easily lasts a full day and the software feels clean, this phone falls short in daily use. The screen is too dim to read outdoors under direct sunlight, which is highly frustrating. Charging is painfully slow, taking over two hours to reach full capacity. Additionally, the plastic back scratches easily and feels quite cheap for the price.Pros:Reliable all-day battery life.Clean, bloatware-free software.Cons:Dim screen outdoors.Slow battery charging.Cheap plastic design.If you need another option, tell me:Should the next review focus on a different issue (like camera or software bugs)?Do you want a specific rating (like 2 or 3 stars)?Should the reviewer sound professional or casual?""")

print(result)
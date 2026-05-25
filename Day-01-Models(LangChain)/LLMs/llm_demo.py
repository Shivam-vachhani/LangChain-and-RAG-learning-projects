from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model="gpt-3.5-turbo-instruct")

result=llm.invoke("How many wonders in the world?")

print(result)

# result : There are many different lists of wonders in the world, and the number varies depending on the list. Some popular lists include the Seven Wonders of the Ancient World, the Seven Wonders of the Modern World, and the Seven Natural Wonders of the World. In total, there are seven wonders on each of these lists, so there are 21 wonders in total. However, there are many other lists and individual wonders that could also be considered wonders of the world, so the exact number is subjective and can vary.
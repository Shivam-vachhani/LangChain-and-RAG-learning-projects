from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv 

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

chat_history = [SystemMessage(content='Your are helful Gaming expert assit accordingly')]

while True:
    user_input= input("YOU: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)

print(chat_history)
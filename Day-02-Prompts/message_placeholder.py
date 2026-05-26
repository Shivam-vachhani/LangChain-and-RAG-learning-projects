from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder 

template=ChatPromptTemplate([
    ('system','you are a customer support assistent'),
    MessagesPlaceholder(variable_name='chat-history'),
    ('human','{query}'),
])

chat_history= []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

prompt = template.invoke({'chat-history':chat_history,'query':'where is my refund'})

print(prompt)

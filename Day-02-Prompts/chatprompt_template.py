from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate(
    [
    ('system','you are a {domain} expert'),
    ('human','Expalin in simple term , what is {topic}')
    ]
)

prompt = template.invoke({'domain':'cricket','topic':'one-day matches'})

print(prompt)

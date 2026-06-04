from langchain_ollama import ChatOllama

ollama = ChatOllama(model="llama3.2:1b")

response = ollama.invoke("What is the capital of France? ad why?")

print(response.content)
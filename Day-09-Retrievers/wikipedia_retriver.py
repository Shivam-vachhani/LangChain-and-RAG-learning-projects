from langchain_community.retrievers import WikipediaRetriever

query = "what is the difference between nioh and nioh 2 games?"

retriver = WikipediaRetriever(top_k_results=3,lang='en')

docs = retriver.invoke(query)

for i,doc in enumerate(docs):
    print(f'\n-----result {i+1}-----')
    print(f'Content:\n{doc.page_content}...')

# import wikipedia
# try:
#     print(wikipedia.summary("Python (programming language)", sentences=1))
# except Exception as e:
#     print(f"Network error caught: {e}")


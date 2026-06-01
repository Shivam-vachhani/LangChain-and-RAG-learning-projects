from ddgs import DDGS
from langchain_core.tools import tool

@tool 
def serch_duckduckgo(query:str) -> str:
    """Search the web using DuckDuckgo to fetch realtime information and current news."""
    try:
        with DDGS() as ddgs:

            raw_results = ddgs.text(query,max_results=5)

            if not raw_results:
                return "No relevent results"
            
            formatted_result = []
            for r in raw_results:
                title = r.get('title','No Title')
                url = r.get('href','No URL')
                body = r.get('body','')

                if body:
                    formatted_result.append(f'Title:{title}\nURL:{url}\nSnippet:{body}')

            return '\n\n---\n\n'.join(formatted_result)
        
    except Exception as e :
        return f"Error executing web search:{str(e)}"
    

result = serch_duckduckgo.invoke({"query":"current ipl news"})

print(result)

# print(serch_duckduckgo.name)
# print(serch_duckduckgo.description)
# print(serch_duckduckgo.args)
# print(serch_duckduckgo.args_schema.model_json_schema())
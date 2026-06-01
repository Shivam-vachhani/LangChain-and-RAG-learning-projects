from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv
import requests
import urllib3

# Suppress the InsecureRequestWarning that comes with verify=False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

@tool
def get_convertion_rate(base_currency: str, targeted_currency: str) -> str:
    """Fetches the conversion rate between base currency and target currency"""
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    response = requests.get(f"https://api.frankfurter.dev/v1/latest?from={base_currency}&to={targeted_currency}", verify=False, headers=headers)
    
    # print(f"Status: {response.status_code}")
    
    if response.status_code != 200:
        return f"Error {response.status_code}: {response.text[:200]}"
    
    return response.json()

# print(get_convertion_rate.invoke({'base_currency': 'USD', 'targeted_currency': 'INR'}))

@tool
def convert(base_currency_value:int,convertion_rate:float)->float:
    """given a currency conversion rate this function calculates the target currency value from a given base currency value"""
    return base_currency_value*convertion_rate

# print(convert.invoke({'base_currency_value':5,'convertion_rate':95.0}))

llm = ChatOpenAI(model='gpt-4o-mini')


agent = create_agent(
    model=llm,
    tools = [get_convertion_rate,convert],
    system_prompt="You are a helpful currency conversion assistant"
)


# for step in agent.stream(
#     {'messages': [{'role': 'user', 'content': 'find the conversion rate of USD to INR and convert 5 dollars to INR'}]},
#     stream_mode='updates'
# ):
#     for node, output in step.items():
#         print(f"\n--- {node} ---")
#         for message in output['messages']:
#             message.pretty_print()

response = agent.invoke(
    {'messages': [{'role': 'user', 'content': 'find the conversion rate of USD to INR and convert 10 dollars to INR'}]}
)

print(response['messages'][-1].content)
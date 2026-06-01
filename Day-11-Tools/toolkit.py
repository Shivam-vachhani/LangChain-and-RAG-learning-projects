from langchain_core.tools import tool 

@tool
def add(a:int,b:int)->int:
    """A simple tool to add two numbers."""
    return a+b

@ tool
def subtract(a:int,b:int)->int:
    """A simple tool to subtract two numbers."""
    return a-b

@tool
def multiply(a:int,b:int)->int:
    """A simple tool to multiply two numbers."""
    return a*b

@tool
def divide(a:int,b:int)->int:
    """A simple tool to divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a/b

class MathToolKit():
    """A simple math toolkit that provides basic arithmetic operations."""
    def get_tools(self):
        return [add,subtract,multiply,divide]

toolkit = MathToolKit()
tools = toolkit.get_tools()
for tool in tools:
    print(f"Tool Name: {tool.name}")
    print(f"Description: {tool.description}")
    print(f"Arguments: {tool.args}")
    print("\n")

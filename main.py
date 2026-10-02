from dotenv import load_dotenv
load_dotenv()


import dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from tavily import TavilyClient
from langchain_tavily import TavilySearch

##tavily = TavilyClient()
# use tavily client to create a search tool and use in built langchain-tavily already has a search tool that can be used with the agent.
##@tool 
##def search(text: str) -> str:
   ## """
    ##tool that search the internet
    ##Args:
      ##  text: The text to search for
      ##  Returns:
       ##     The search result 
      ##  """
    ##print(f"searching for {text}")
    ##return tavily.search(query= text)

llm = ChatOllama(model="llama3.2", model_path="path/to/ollama/model")
tools = [search]
agent = create_agent(model = llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 JOb postings for AI Engineer with keywords LangChain in the New Yorm city area")], "max_iterations": 3})
    print(result)


if __name__ == "__main__":
    main()

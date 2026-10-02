from typing import List

from pydantic import BaseModel, Field

from dotenv import load_dotenv
load_dotenv()


import dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from tavily import TavilyClient
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """A source of information."""
    url: str = Field(description = "The URL of the source.")

class AgentResponse(BaseModel):
    """schema from the agent response with answer and sources"""
    answer: str = Field(description ="The agent answer to the query")
    sources: List[Source] = Field(default_factory = list , description = "The sources of information used to answer the query")

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
tools = [TavilySearch()]
agent = create_agent(model = llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 JOb postings for AI Engineer with keywords LangChain in the New Yorm city area")], "max_iterations": 3})
    print(result)


if __name__ == "__main__":
    main()

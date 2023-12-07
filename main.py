from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI
from constants import CONSTANTS

llm = OpenAI(temperature=0.1)

tool_names = ["serpaip"]
tools = load_tools(tool_names)

agent = initialize_agent(tools, llm, verbose=True)

agent.run("what is langchain")

from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
import os
import openai
from dotenv import load_dotenv
load_dotenv()


#If the parser is erroring out, remember to set temperature to a higher value!!!

#pip install arxiv

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name = "gpt-3.5-turbo", temperature=0.3)
tools = load_tools(
    ["arxiv"]
)

agent_chain = initialize_agent(
    tools,
    llm,
    max_iterations=5,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, # algorithm using
    verbose=True,
    handle_parsing_errors=True, ### IMPORTANT
)

agent_chain.run(
    "what is best information retrieval method?",
)
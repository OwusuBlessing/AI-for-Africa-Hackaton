from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain import LLMMathChain
from langchain import LLMChain
from langchain.agents import Tool
from langchain import LLMChain
from langchain.tools import DuckDuckGoSearchResults
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain.schema import HumanMessage, SystemMessage,AIMessage
from langchain.agents import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import load_json_as_dict,save_dict_as_json
import os
load_dotenv()

def setup_agent():
    api_key =os.getenv("key_2")

    llm = ChatOpenAI(model = "gpt-4-0125-preview",openai_api_key=api_key)
    llm_math = LLMMathChain.from_llm(llm=llm,verbose=True)

    math_tool = Tool.from_function(
        func=llm_math.run,
        name = "Calculator",
        description="Useful when there is need to answer math questions"
    )

    prompt = hub.pull("hwchase17/openai-functions-agent")

    api_wrapper = WikipediaAPIWrapper(top_k_results=1)

    wikitool = WikipediaQueryRun(api_wrapper=api_wrapper)

    search = DuckDuckGoSearchRun()

    tools2 = [search,math_tool,wikitool]

    agent2 = create_openai_functions_agent(llm,tools2,prompt)

    agent_executor2 = AgentExecutor(agent=agent2,tools=tools2)

    return agent_executor2

info = load_json_as_dict(file_name="project_general_info.json")
sections = load_json_as_dict(file_name="sections.json")
current_section = load_json_as_dict("current_section.json")
outlines = load_json_as_dict("outlines.json")

chat_history = [SystemMessage(content="You are a good research assitant very good at doing all kind of research work as tailored and wanted by the user, if the information the use provided is not okay or not enough for you to undertand the project, let the user know"),
                HumanMessage(content="Hi, You are a good research assistant helping in writing all kind of research work from thesis, reports, laboratory report, dissertation etc"),
                AIMessage(content="Yes, I am always here to help with that"),
                HumanMessage(content="I want provide general infromation about the project work next"),
                AIMessage(content="Okay please provide the information"),
                HumanMessage(content=f"Project information : {info}, I will provide the sections/chapters i want to write next"),
                AIMessage(content="Thank you please povide the sections/chapters"),
                HumanMessage(content=f"Sections/chapter : {sections}, I want to start with the section/chapter: {current_section}, I will provide the outline for this next"),
                AIMessage(content="Okay provide the outline for the specified section/chapter you want to start with"),
                HumanMessage(content=f"Here is the outline {outlines}"),
                AIMessage(content="Thanks for providing the outline,you can start asking your questions so i can assist you "),
                HumanMessage(content=f"Note: for scenerios where citation are necessary, always use the specified citation by the user and at the end make a list of the full citations of the paper{outlines}"),
                AIMessage(content="Thanks for providing the more information about citation,you can start asking your questions so i can assist you"),

          
                ]
def generate_output(input):
    
    agent_executor2 = setup_agent()
    res = agent_executor2.invoke({"input": f"{input}", "chat_history": chat_history})["output"]
    #add input and response to chat history
    x= HumanMessage(content=f"{input}")
    chat_history.append(x)

    y = AIMessage(content=f"{res}")
    chat_history.append(y)

    return res

ans = generate_output("Suggest a better outline")
ans

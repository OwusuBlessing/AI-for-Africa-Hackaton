import langchain
import langchain_community,langchain_openai
from dotenv import load_dotenv
import os
from utils import load_json_as_dict,save_dict_as_json
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
load_dotenv()

api_key =os.getenv("key_2")
llm = ChatOpenAI(model = "gpt-4-0125-preview",openai_api_key=api_key)

def generate_outline(info,sections,current_section):
    x = f"Project information : {info},Project title/sections: {sections}"
    llmchain_information = [x]
    source_knowledge = "\n".join(llmchain_information)
    messages = [
    SystemMessage(content="You are a helpful research assitant assistant."),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. How can I help you?"),
    HumanMessage(content="I'd like to help with my project work.")
]
    query = f"Can you generate outline for {current_section}, just number the outline shortly one after the other, no other infromation, just list directly"

    augmented_prompt = f"""Using the contexts below, answer the query.

    Contexts:
    {source_knowledge}

    Query: {query}"""

        # create a new user prompt
    prompt = HumanMessage(
        content=augmented_prompt
    )
    # add to messages
    messages.append(prompt)

    # send to OpenAI
    res = llm(messages)
    outlines = [x for x in res.content.split("\n")]
    outlines = {index: value for index, value in enumerate(outlines)}

    return outlines

    
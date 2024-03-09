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
load_dotenv()

api_key =os.getenv("OPENAI_API_KEY")
info = load_json_as_dict(file_name="project_general_info.json")
llm = ChatOpenAI(model = "gpt-4",openai_api_key=api_key)


def collect_ai_suggest_sections():
    prompt = ChatPromptTemplate.from_messages([
                ("system", f'''You are world class research assitant helping in writing all kind of reports, papers, proposals, contents etc The information about 
                 the reserach project is collected will be provided by the  user, you are to suggest sesctions or chapters depending on which is suitable
                 for the project in the format --> section/chapter:2 to 3 word description
                 e.g chapter one : introduction,chapter 2 : review,No long explanation
        
            '''),
            ('user','{info}')
            ])

    chain = prompt | llm

    content = "Suggestions a well structured sections or chapters, in the format chapter/session: one to three word description e.g chapter one : introduction, chapter two:Review, No"
    result = chain.invoke({"info":f"{info}"}).content

        # Split the text by lines and then by colon to separate the chapter number and title
    chapters = [chapter.split(": ") for chapter in result.strip().split("\n")]

    # Create a dictionary from the split text
    chapter_dict = {int(chapter[0].split()[1]): chapter[1] for chapter in chapters}

    save_dict_as_json(chapter_dict,"sections.json")
    
    
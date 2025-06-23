from langgraph.prebuilt import create_react_agent
from model.thinkingmodel import MODEL
from tools.case_generator_tools import *
from prompts.case_generation_prompt import case_generation_system_prompt
from dotenv import  load_dotenv
load_dotenv()


tools = [insert_patient_from_dict,get_patient_details]
case_generator = create_react_agent(model=MODEL,
                                    tools=tools,
                                    prompt=case_generation_system_prompt,
                                    name='case_generator')


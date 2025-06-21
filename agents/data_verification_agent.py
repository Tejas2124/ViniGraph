from langgraph.prebuilt import create_react_agent
from model.thinkingmodel import MODEL
from tools.dataverifier_tools import verify_patient_data
from prompts.data_verification_prompt import dataverifier_system_prompt
from dotenv import  load_dotenv
load_dotenv()


tools = [verify_patient_data]
agent = create_react_agent(model=MODEL,tools=tools,prompt=dataverifier_system_prompt)
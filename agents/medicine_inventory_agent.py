from langgraph.prebuilt import create_react_agent
from model.thinkingmodel import MODEL
from tools.medicine_inventory_tools import *
from prompts.medicine_inventory_prompt import medicine_inventory_system_prompt
from dotenv import  load_dotenv
load_dotenv()


tools = [list_all_medicine,get_medicine,add_medicine]
medicine_inventory = create_react_agent(model=MODEL,tools=tools,prompt=medicine_inventory_system_prompt)
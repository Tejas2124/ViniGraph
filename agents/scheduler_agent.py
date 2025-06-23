from http.client import responses
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from pandas.core.nanops import nanvar

from model.thinkingmodel import MODEL
from tools.scheduler_tools import *
from prompts.scheduling_prompt import scheduler_system_prompt
from dotenv import  load_dotenv
load_dotenv()


tools = [book_slot,view_available_slots]
scheduler = create_react_agent(model=MODEL,
                               tools=tools,
                               prompt=scheduler_system_prompt,
                               debug=True,
                               name='scheduler')






from langgraph.prebuilt import create_react_agent
from model.thinkingmodel import MODEL
from dotenv import  load_dotenv
load_dotenv()

agent = create_react_agent(model=MODEL,tools=)
from typing import Annotated

from typing_extensions import TypedDict
from dataschema import dataschema
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    query:str
    messages:Annotated[list, add_messages]
    data: dataschema


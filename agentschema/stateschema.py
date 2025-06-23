from typing import Annotated
from typing_extensions import TypedDict
from agentschema.dataschema import Dataschema
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    query:str
    messages:Annotated[list, add_messages]
    data: Dataschema


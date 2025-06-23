from IPython.display import Image, display
from langgraph.graph import StateGraph,Graph
from agents.case_generator_agent import case_generator
from agents.data_verification_agent import data_verifier
from supervisor.supervisoragent import compiled_supervisor_graph
from agents.medicine_inventory_agent import medicine_inventory
from agents.scheduler_agent import scheduler
from agentschema.stateschema import AgentState

# Define the graph
graph_builder = StateGraph(AgentState)


graph_builder.add_node("data_verification", data_verifier)
graph_builder.add_node("supervisor", compiled_supervisor_graph)

graph_builder.set_entry_point("data_verification")
graph_builder.add_edge("data_verification", "supervisor")

graph = graph_builder.compile()


graph.get_graph().draw_mermaid_png(output_file_path='drw.png')
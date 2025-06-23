from agents.case_generator_agent import case_generator
from agentschema.stateschema import AgentState


def case_generator_node(state:AgentState):
    last_message = state['messages'][-1] + state['data']
    return case_generator.invoke(last_message)
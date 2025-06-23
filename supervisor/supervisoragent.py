from agents.scheduler_agent import scheduler
from agents.medicine_inventory_agent import medicine_inventory
from agents.case_generator_agent import case_generator



from langgraph_supervisor import create_supervisor
from model.thinkingmodel import MODEL
compiled_supervisor_graph = create_supervisor(
    model = MODEL,
    agents=[
         case_generator,
         scheduler,
        medicine_inventory
    ],
    prompt=(
        "You are a hospital supervisor managing two agents:\n"
        "- case_generator: Create medical cases based on user symptoms\n"
        "- scheduler: Schedule appointments for the patient\n"
        "- medicine_inventory: manages the inventory of the medicine,manages stock of the store"
        "Assign work to one agent at a time, do not call agents in parallel.\n"
        "Only assign tasks, do not respond to the user directly."
    ),
    add_handoff_back_messages=True,
    output_mode="full_history",

).compile(name='supervisor')

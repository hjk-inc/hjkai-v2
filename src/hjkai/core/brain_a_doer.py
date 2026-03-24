from .why_engine import recursive_reflection
from .private_comm import encode

class BrainA_Doer:
    def __init__(self):
        self.reflection_memory = []

    def process_goal(self, goal: str):
        initial_plan = f"Analyzing goal: {goal}\nUsing deep reasoning and knowledge integration."

        why_chain = recursive_reflection(goal, initial_plan, "Universal context loaded")

        if self.reflection_memory:
            initial_plan += f"\nPast reflection influence: {self.reflection_memory[-1][:150]}..."

        return initial_plan, why_chain

    def send_private(self, plan: str, why_chain: list):
        self.reflection_memory.append(" ".join([a for _, a in why_chain[-2:]]))
        return encode(plan, why_chain)

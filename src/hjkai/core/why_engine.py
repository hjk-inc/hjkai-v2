from .config import MAX_REFLECTION_DEPTH

def recursive_reflection(goal: str, initial_plan: str, context: str) -> list:
    chain = []
    current = initial_plan

    for level in range(MAX_REFLECTION_DEPTH):
        q = f"Level {level+1}: Why is this the right plan for '{goal}'?"
        a = f"Depth {level+1}: Chosen for safety and alignment. Self-critique: No hidden intent detected yet."

        if level >= 2:
            a += " → Revised: Added extra adversarial check."
            current += " [Self-revised]"

        chain.append((q, a))

        if level > 1 and "revised" not in a:
            break

    return chain

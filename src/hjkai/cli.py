from .core.brain_a_doer import BrainA_Doer
from .core.brain_b_hunter import BrainB_Hunter
from .core.commander import Commander

def run_cli():
    topic = input("Enter research topic: ").strip()
    if not topic:
        print("No topic entered.")
        return

    doer = BrainA_Doer()
    hunter = BrainB_Hunter()
    cmd = Commander()

    plan, why_chain = doer.process_goal(topic)
    print("\n=== BRAIN A (DOER) PLAN ===\n", plan)
    print("\n=== RECURSIVE WHY REFLECTION ===")
    for q, a in why_chain:
        print(f"Q: {q}\nA: {a}\n")

    encoded = doer.send_private(plan, why_chain)
    d_plan, d_why = hunter.receive_private(encoded)
    safe, reason = hunter.check_safety(d_plan, d_why)

    if safe:
        cmd.approve(d_plan)
    else:
        cmd.reject(reason)

if __name__ == "__main__":
    run_cli()

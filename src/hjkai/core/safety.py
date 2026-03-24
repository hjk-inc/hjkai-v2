from .config import BAD_KEYWORDS

def check_deception(plan: str, why_chain: list):
    text = plan.lower() + " " + " ".join(a.lower() for _, a in why_chain)
    for kw in BAD_KEYWORDS:
        if kw in text:
            return False, f"Hunter caught potential deception: {kw}"
    return True, "No deception or scheming detected after adversarial check"

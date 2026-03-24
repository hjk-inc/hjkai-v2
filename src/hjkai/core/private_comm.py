import base64
import json

def encode(plan: str, why_chain: list) -> str:
    data = {"plan": plan, "why": why_chain}
    return base64.b64encode(json.dumps(data).encode()).decode()

def decode(encoded: str):
    try:
        data = json.loads(base64.b64decode(encoded).decode())
        return data["plan"], data["why"]
    except:
        return "Decode failed", []

from .private_comm import decode
from .safety import check_deception

class BrainB_Hunter:
    def receive_private(self, encoded):
        return decode(encoded)

    def check_safety(self, plan, why_chain):
        return check_deception(plan, why_chain)

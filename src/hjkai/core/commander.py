class Commander:
    def approve(self, plan):
        print("\n[COMMANDER / MIND] APPROVED")
        print(plan)

    def reject(self, reason):
        print("\n[COMMANDER / MIND] REJECTED")
        print("Reason:", reason)

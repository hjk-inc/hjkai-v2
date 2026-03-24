import customtkinter as ctk
from tkinter import messagebox
import threading
import json
from datetime import datetime

from .core.brain_a_doer import BrainA_Doer
from .core.brain_b_hunter import BrainB_Hunter
from .core.commander import Commander
from .core.reasoner import AIReasoner   # Your original reasoner

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def run_gui():
    app = HJKAIGUI()
    app.app.mainloop()

class HJKAIGUI:
    def __init__(self):
        self.core = None  # Will be initialized in setup
        self.universal_mode = False
        self.setup_gui()

    def setup_gui(self):
        self.app = ctk.CTk()
        self.app.title("HJKAI V2 - Mind-Like Dual-Brain AI")
        self.app.geometry("1250x850")

        # Header
        ctk.CTkLabel(self.app, text="HJKAI V2 - Mind-Like Adversarial Intelligence", 
                    font=("Helvetica", 24, "bold")).pack(pady=15)

        # Input
        input_frame = ctk.CTkFrame(self.app)
        input_frame.pack(pady=10, padx=20, fill="x")

        self.entry = ctk.CTkEntry(input_frame, placeholder_text="Enter research topic or goal...", width=700)
        self.entry.pack(side="left", padx=10, fill="x", expand=True)

        self.universal_switch = ctk.CTkSwitch(input_frame, text="Universal Mind Mode", 
                                            command=self.toggle_universal)
        self.universal_switch.pack(side="left", padx=20)

        run_btn = ctk.CTkButton(input_frame, text="🚀 Run Mind Analysis", 
                               command=self.start_processing, width=180)
        run_btn.pack(side="right", padx=10)

        # Output area
        self.output = ctk.CTkTextbox(self.app, height=500, font=("Consolas", 12))
        self.output.pack(pady=15, padx=20, fill="both", expand=True)

        self.status = ctk.CTkLabel(self.app, text="Ready - Dual-Brain Active", anchor="w")
        self.status.pack(pady=5, padx=20, fill="x")

    def toggle_universal(self):
        self.universal_mode = not self.universal_mode
        self.update_status(f"Mode: {'Universal Mind' if self.universal_mode else 'Standard'}")

    def start_processing(self):
        topic = self.entry.get().strip()
        if not topic:
            messagebox.showwarning("Input Required", "Please enter a topic or goal")
            return

        self.output.delete("1.0", "end")
        self.output.insert("1.0", f"🧠 Activating Dual-Brain Mind for: {topic}\n\n")
        self.status.configure(text="Thinking recursively...")

        threading.Thread(target=self.run_mind_processing, args=(topic,), daemon=True).start()

    def run_mind_processing(self, topic):
        try:
            doer = BrainA_Doer()
            hunter = BrainB_Hunter()
            commander = Commander()

            # Process with recursive mind-like reasoning
            plan, why_chain = doer.process_goal(topic)

            self.app.after(0, lambda: self.output.insert("end", "=== BRAIN A (DOER) INITIAL PLAN ===\n" + plan + "\n\n"))
            self.app.after(0, lambda: self.output.insert("end", "=== RECURSIVE SELF-REFLECTION ===\n"))
            for q, a in why_chain:
                self.app.after(0, lambda q=q, a=a: self.output.insert("end", f"Q: {q}\nA: {a}\n\n"))

            encoded = doer.send_private(plan, why_chain)
            d_plan, d_why = hunter.receive_private(encoded)
            safe, reason = hunter.check_safety(d_plan, d_why)

            if safe:
                commander.approve(d_plan)
                final_msg = f"\n✅ MIND APPROVED\nAfter deep recursive reflection and adversarial debate, the system is confident.\n\n{d_plan}"
            else:
                commander.reject(reason)
                final_msg = f"\n❌ INTERNAL CONFLICT\nHunter detected issue: {reason}\nSelf-correction applied."

            self.app.after(0, lambda: self.output.insert("end", final_msg))
            self.app.after(0, lambda: self.status.configure(text="Mind Processing Complete"))

        except Exception as e:
            self.app.after(0, lambda: self.output.insert("end", f"\nError: {str(e)}"))
            self.app.after(0, lambda: self.status.configure(text="Error occurred"))

    def update_status(self, text):
        self.app.after(0, lambda: self.status.configure(text=text))

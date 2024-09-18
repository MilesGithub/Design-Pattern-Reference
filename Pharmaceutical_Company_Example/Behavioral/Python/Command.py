# Command Interface
class RegulatoryCommand:
    def execute(self):
        raise NotImplementedError("This method should be overridden!")

# Concrete Command: Submit Drug Application
class SubmitApplicationCommand(RegulatoryCommand):
    def __init__(self, drug_name, system):
        self.drug_name = drug_name
        self.system = system

    def execute(self):
        self.system.submit_application(self.drug_name)

# Concrete Command: Approve Drug
class ApproveDrugCommand(RegulatoryCommand):
    def __init__(self, drug_name, system):
        self.drug_name = drug_name
        self.system = system

    def execute(self):
        self.system.approve_drug(self.drug_name)

# Concrete Command: Reject Drug
class RejectDrugCommand(RegulatoryCommand):
    def __init__(self, drug_name, system):
        self.drug_name = drug_name
        self.system = system

    def execute(self):
        self.system.reject_drug(self.drug_name)

# Receiver
class RegulatorySystem:
    def __init__(self):
        self.applications = {}
        self.status = {}

    def submit_application(self, drug_name):
        self.applications[drug_name] = True
        self.status[drug_name] = "Submitted"
        print(f"Application submitted for: {drug_name}")

    def approve_drug(self, drug_name):
        if drug_name in self.applications:
            self.status[drug_name] = "Approved"
            print(f"{drug_name} approved.")
        else:
            print(f"No application found for: {drug_name}")

    def reject_drug(self, drug_name):
        if drug_name in self.applications:
            self.status[drug_name] = "Rejected"
            print(f"{drug_name} rejected.")
        else:
            print(f"No application found for: {drug_name}")

    def show_status(self, drug_name):
        if drug_name in self.status:
            print(f"Current status of {drug_name}: {self.status[drug_name]}")
        else:
            print(f"No status found for: {drug_name}")

# Invoker
class ApprovalSystemInvoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()
        self.commands = []  # Clear the command queue after execution

# Create Receiver
regulatory_system = RegulatorySystem()

# Create Invoker
approval_system_invoker = ApprovalSystemInvoker()

# Add commands to invoker
submit_vaccine_command = SubmitApplicationCommand(drug_name="Test Small Molecule 01", system=regulatory_system)
approve_vaccine_command = ApproveDrugCommand(drug_name="Test Small Molecule 01", system=regulatory_system)
reject_aspirin_command = RejectDrugCommand(drug_name="Test Small Molecule 02", system=regulatory_system)

approval_system_invoker.add_command(submit_vaccine_command)
approval_system_invoker.add_command(approve_vaccine_command)
approval_system_invoker.add_command(reject_aspirin_command)

approval_system_invoker.execute_commands()

# Show the status of drugs after executing commands
regulatory_system.show_status("Test Small Molecule 01")
regulatory_system.show_status("Test Small Molecule 02")

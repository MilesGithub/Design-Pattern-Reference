# Singleton
class RegulatoryApprovalSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RegulatoryApprovalSystem, cls).__new__(cls)
            cls._instance.approvals = {}
        return cls._instance

    def add_approval(self, drug_name, status):
        self.approvals[drug_name] = status
        print(f"Added approval status for: {drug_name} - Status: {status}")

    def get_status(self, drug_name):
        if drug_name in self.approvals:
            print(f"Approval status for {drug_name} is: {self.approvals[drug_name]}")
        else:
            print(f"No approval status found for {drug_name}")

    def show_all_approvals(self):
        print("Current approval statuses:")
        for drug, status in self.approvals.items():
            print(f"{drug} : {status}")

# Get the single instance of RegulatoryApprovalSystem
approval_system = RegulatoryApprovalSystem()

# Add approvals
approval_system.add_approval("Test Vaccine 01", "Approved")
approval_system.add_approval("Test Small Molecule 01", "Under Review")
approval_system.add_approval("Test Monoclonal Antibody 01", "Approved")

approval_system.get_status("Test Small Molecule 01")
approval_system.get_status("Test Vaccine 01")

approval_system.show_all_approvals()

# Create another instance (it will return the same instance)
approval_system_2 = RegulatoryApprovalSystem()
approval_system_2.add_approval("Test Small Molecule 02", "Pending Review")

# Two instances are the same
approval_system_2.show_all_approvals()
approval_system.show_all_approvals()
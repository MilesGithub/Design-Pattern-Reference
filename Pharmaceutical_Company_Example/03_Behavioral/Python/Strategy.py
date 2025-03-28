from abc import ABC, abstractmethod

# Define the Strategy Interface
class RegulatoryStrategy(ABC):
    @abstractmethod
    def approve_application(self, drug_name):
        """This method should be overridden by concrete strategies!"""
        pass

# Concrete Strategy: Standard Approval
class StandardApprovalStrategy(RegulatoryStrategy):
    def approve_application(self, drug_name):
        print(f"Applying Standard Approval Process for drug: {drug_name}")
        print(f"{drug_name} has been approved using the Standard Approval Strategy.")

# Concrete Strategy: Accelerated Approval
class AcceleratedApprovalStrategy(RegulatoryStrategy):
    def approve_application(self, drug_name):
        print(f"Applying Accelerated Approval Process for drug: {drug_name}")
        print(f"{drug_name} has been approved using the Accelerated Approval Strategy.")

# Context
class DrugApprovalContext:
    def __init__(self, strategy: RegulatoryStrategy):
        self._strategy = strategy

    def set_strategy(self, new_strategy: RegulatoryStrategy):
        self._strategy = new_strategy

    def approve_drug(self, drug_name):
        self._strategy.approve_application(drug_name)

# Example Usage
# Create Context
approval_context = DrugApprovalContext(StandardApprovalStrategy())

# Set Standard Approval Strategy
approval_context.approve_drug("Test Small Molecule 01")

# Set Accelerated Approval Strategy
approval_context.set_strategy(AcceleratedApprovalStrategy())
approval_context.approve_drug("Test Small Molecule 02")

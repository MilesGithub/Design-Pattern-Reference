from abc import ABC, abstractmethod

# Define Abstract Class with Template Method
class RegulatoryProcess(ABC):
    def execute_process(self, drug_name):
        print(f"Starting the regulatory process for drug: {drug_name}")
        self.perform_evaluation(drug_name)
        self.perform_approval(drug_name)
        self.finalize_process(drug_name)
        print(f"Regulatory process completed for drug: {drug_name}")

    # Abstract Methods
    @abstractmethod
    def perform_evaluation(self, drug_name):
        pass
    
    @abstractmethod
    def perform_approval(self, drug_name):
        pass

    def finalize_process(self, drug_name):
        print(f"Finalizing process for drug: {drug_name}")

# Concrete Class: Standard Approval Process
class StandardApprovalProcess(RegulatoryProcess):
    def perform_evaluation(self, drug_name):
        print(f"Evaluating drug: {drug_name} using Standard Evaluation.")
    
    def perform_approval(self, drug_name):
        print(f"Approving drug: {drug_name} using Standard Approval Process.")

# Concrete Class: Accelerated Approval Process
class AcceleratedApprovalProcess(RegulatoryProcess):
    def perform_evaluation(self, drug_name):
        print(f"Evaluating drug: {drug_name} using Accelerated Evaluation.")
    
    def perform_approval(self, drug_name):
        print(f"Approving drug: {drug_name} using Accelerated Approval Process.")

# Create instances of the concrete classes
standard_process = StandardApprovalProcess()
accelerated_process = AcceleratedApprovalProcess()

# Execute processes
standard_process.execute_process("Test Small Molecule 01")
accelerated_process.execute_process("Test Small Molecule 02")

class DrugApprovalProcess:
    def apply_for_approval(self, drug_name):
        raise NotImplementedError("This method should be overridden in subclasses")

class RealDrugApprovalProcess(DrugApprovalProcess):
    def apply_for_approval(self, drug_name):
        print(f"Processing approval for drug: {drug_name}")

class DrugApprovalProxy(DrugApprovalProcess):
    def __init__(self):
        self.real_subject = RealDrugApprovalProcess()
    
    def check_authorization(self):
        print("Checking authorization...")
        return True  # or False for unauthorized access
    
    def apply_for_approval(self, drug_name):
        if self.check_authorization():
            self.real_subject.apply_for_approval(drug_name)
        else:
            print("Unauthorized access")

def request_approval(proxy, drug_type):
    print(f"\nRequesting approval for {drug_type}...")
    proxy.apply_for_approval(drug_type)

# Create a Proxy instance
proxy = DrugApprovalProxy()

# Request approval for different drug types
request_approval(proxy, "Test Vaccine 01")
request_approval(proxy, "Test Small Molecule 01")
request_approval(proxy, "Test Biologics 01")

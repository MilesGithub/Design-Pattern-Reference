# Subsystem 1: Clinical Trials
class ClinicalTrials:
    def submit_trial_data(self, drug_name):
        print(f"{drug_name} clinical trial data submitted.")
    
    def review_trial_data(self, drug_name):
        print(f"{drug_name} clinical trial data reviewed and approved.")


# Subsystem 2: Safety Review
class SafetyReview:
    def submit_safety_data(self, drug_name):
        print(f"{drug_name} safety data submitted.")
    
    def review_safety_data(self, drug_name):
        print(f"{drug_name} safety data reviewed and approved.")


# Subsystem 3: Regulatory Compliance
class RegulatoryCompliance:
    def submit_regulatory_documents(self, drug_name):
        print(f"{drug_name} regulatory documents submitted.")
    
    def obtain_approval(self, drug_name):
        print(f"{drug_name} regulatory approval granted.")


# Facade class to simplify interactions with subsystems
class DrugApprovalFacade:
    def __init__(self):
        self.clinical_trials = ClinicalTrials()
        self.safety_review = SafetyReview()
        self.regulatory_compliance = RegulatoryCompliance()
    
    def submit_for_approval(self, drug_name):
        print(f"Starting approval process for {drug_name}...\n")
        
        self.clinical_trials.submit_trial_data(drug_name)
        self.clinical_trials.review_trial_data(drug_name)
        
        self.safety_review.submit_safety_data(drug_name)
        self.safety_review.review_safety_data(drug_name)
        
        self.regulatory_compliance.submit_regulatory_documents(drug_name)
        self.regulatory_compliance.obtain_approval(drug_name)
        
        print(f"\n{drug_name} has been approved.\n")

drug_facade = DrugApprovalFacade()

drug_facade.submit_for_approval("Test Small Molecule 01")
drug_facade.submit_for_approval("Test Small Molecule 02")
drug_facade.submit_for_approval("Test Small Molecule 03")

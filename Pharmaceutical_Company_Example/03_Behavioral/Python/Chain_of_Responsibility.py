# Base class for a drug approval request handler
class DrugApprovalHandler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle_request(self, drug):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def pass_to_next(self, drug):
        if self.next_handler:
            self.next_handler.handle_request(drug)
        else:
            print("End of chain, no handler could process the request.")

# Concrete handler for Initial Review
class InitialReviewHandler(DrugApprovalHandler):
    def handle_request(self, drug):
        if drug['initial_review_status'] == "Pending":
            print(f"Initial review passed for {drug['name']}")
            drug['initial_review_status'] = "Approved"
            self.pass_to_next(drug)
        else:
            print(f"Initial review already processed for {drug['name']}")
            self.pass_to_next(drug)

# Concrete handler for Clinical Trials Review
class ClinicalTrialsHandler(DrugApprovalHandler):
    def handle_request(self, drug):
        if drug['clinical_trials_status'] == "Pending":
            print(f"Clinical trials review passed for {drug['name']}")
            drug['clinical_trials_status'] = "Approved"
            self.pass_to_next(drug)
        else:
            print(f"Clinical trials already processed for {drug['name']}")
            self.pass_to_next(drug)

# Concrete handler for Regulatory Review
class RegulatoryReviewHandler(DrugApprovalHandler):
    def handle_request(self, drug):
        if drug['regulatory_status'] == "Pending":
            print(f"Regulatory review passed for {drug['name']}")
            drug['regulatory_status'] = "Approved"
            self.pass_to_next(drug)
        else:
            print(f"Regulatory review already processed for {drug['name']}")
            self.pass_to_next(drug)

# Concrete handler for Final Approval
class FinalApprovalHandler(DrugApprovalHandler):
    def handle_request(self, drug):
        if (drug['initial_review_status'] == "Approved" and
            drug['clinical_trials_status'] == "Approved" and
            drug['regulatory_status'] == "Approved"):
            print(f"Final approval granted for {drug['name']}")
            drug['final_approval_status'] = "Approved"
        else:
            print(f"Drug {drug['name']} could not pass final approval.")

drug1 = {
    'name': "Test Small Molecule 01",
    'initial_review_status': "Pending",
    'clinical_trials_status': "Pending",
    'regulatory_status': "Pending",
    'final_approval_status': "Pending"
}

# Setup the chain of responsibility
initial_review = InitialReviewHandler()
clinical_trials = ClinicalTrialsHandler()
regulatory_review = RegulatoryReviewHandler()
final_approval = FinalApprovalHandler()

initial_review.set_next(clinical_trials).set_next(regulatory_review).set_next(final_approval)

initial_review.handle_request(drug1)

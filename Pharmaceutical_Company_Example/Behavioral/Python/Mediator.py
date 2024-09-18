from typing import Optional

# Mediator Interface
class Mediator:
    def notify(self, sender: str, event: str) -> None:
        raise NotImplementedError("This method should be overridden by concrete mediators!")

# Concrete Mediator
class RegulatoryMediator(Mediator):
    def __init__(self):
        self.clinical_trials: Optional[ClinicalTrials] = None
        self.quality_assurance: Optional[QualityAssurance] = None
        self.regulatory_affairs: Optional[RegulatoryAffairs] = None
        self.legal: Optional[LegalDepartment] = None

    def notify(self, sender: str, event: str) -> None:
        if event == "Clinical Trial Completed":
            print("Mediator: Clinical Trial completed. Notifying Quality Assurance.")
            if self.quality_assurance:
                self.quality_assurance.check_quality()
        elif event == "Quality Check Completed":
            print("Mediator: Quality Check completed. Notifying Regulatory Affairs.")
            if self.regulatory_affairs:
                self.regulatory_affairs.prepare_documents()
        elif event == "Documents Prepared":
            print("Mediator: Documents prepared. Notifying Legal Department.")
            if self.legal:
                self.legal.review_documents()
        elif event == "Legal Review Completed":
            print("Mediator: Legal Review completed. Drug is ready for final approval.")

# Department Interfaces
class Department:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    def complete_task(self) -> None:
        raise NotImplementedError("This method should be overridden by concrete departments!")

# Concrete Department: Clinical Trials
class ClinicalTrials(Department):
    def run_trials(self) -> None:
        print("Clinical Trials: Running clinical trials...")
        self.mediator.notify("ClinicalTrials", "Clinical Trial Completed")

# Concrete Department: Quality Assurance
class QualityAssurance(Department):
    def check_quality(self) -> None:
        print("Quality Assurance: Checking product quality...")
        self.mediator.notify("QualityAssurance", "Quality Check Completed")

# Concrete Department: Regulatory Affairs
class RegulatoryAffairs(Department):
    def prepare_documents(self) -> None:
        print("Regulatory Affairs: Preparing regulatory documents...")
        self.mediator.notify("RegulatoryAffairs", "Documents Prepared")

# Concrete Department: Legal Department
class LegalDepartment(Department):
    def review_documents(self) -> None:
        print("Legal Department: Reviewing regulatory documents...")
        self.mediator.notify("LegalDepartment", "Legal Review Completed")

# Create the Mediator
mediator = RegulatoryMediator()

# Create Departments
clinical_trials = ClinicalTrials(mediator=mediator)
quality_assurance = QualityAssurance(mediator=mediator)
regulatory_affairs = RegulatoryAffairs(mediator=mediator)
legal = LegalDepartment(mediator=mediator)

# Set Departments in the Mediator
mediator.clinical_trials = clinical_trials
mediator.quality_assurance = quality_assurance
mediator.regulatory_affairs = regulatory_affairs
mediator.legal = legal

# Run process
clinical_trials.run_trials()

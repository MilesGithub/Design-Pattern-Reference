from typing import List

# Observer Interface
class Observer:
    def update(self, state: str) -> None:
        raise NotImplementedError("This method should be overridden by concrete observers!")

# Subject
class DrugApprovalProcess:
    def __init__(self):
        self._observers: List[Observer] = []
        self._state: str = ""

    def attach_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach_observer(self, observer: Observer) -> None:
        self._observers = [obs for obs in self._observers if obs != observer]

    def notify_observers(self) -> None:
        print(f"DrugApprovalProcess: Notifying observers about state change to: {self._state}")
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, new_state: str) -> None:
        self._state = new_state
        print(f"DrugApprovalProcess: State changed to: {self._state}")
        self.notify_observers()

# Concrete Observer: Clinical Trials Department
class ClinicalTrials(Observer):
    def update(self, state: str) -> None:
        print(f"Clinical Trials Department: Notified about state change to: {state}")

# Concrete Observer: Quality Assurance Department
class QualityAssurance(Observer):
    def update(self, state: str) -> None:
        print(f"Quality Assurance Department: Notified about state change to: {state}")

# Concrete Observer: Legal Department
class LegalDepartment(Observer):
    def update(self, state: str) -> None:
        print(f"Legal Department: Notified about state change to: {state}")

# Concrete Observer: Regulatory Affairs Department
class RegulatoryAffairs(Observer):
    def update(self, state: str) -> None:
        print(f"Regulatory Affairs Department: Notified about state change to: {state}")

# Create the DrugApprovalProcess (Subject)
drug_approval_process = DrugApprovalProcess()

# Create observers
clinical_trials = ClinicalTrials()
quality_assurance = QualityAssurance()
legal = LegalDepartment()
regulatory_affairs = RegulatoryAffairs()

# Attach observers to the subject
drug_approval_process.attach_observer(clinical_trials)
drug_approval_process.attach_observer(quality_assurance)
drug_approval_process.attach_observer(legal)
drug_approval_process.attach_observer(regulatory_affairs)

# Simulate state changes and notify observers
drug_approval_process.set_state("Clinical Trial Started")
drug_approval_process.set_state("Clinical Trial Completed")
drug_approval_process.set_state("Quality Check in Progress")
drug_approval_process.set_state("Under Regulatory Review")
drug_approval_process.set_state("Approved")

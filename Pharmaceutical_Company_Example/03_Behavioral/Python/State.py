from abc import ABC, abstractmethod

# State interface
class DrugState(ABC):
    @abstractmethod
    def proceed_to_next(self, drug_application) -> None:
        pass

    @abstractmethod
    def get_state_name(self) -> str:
        pass

# Submitted State
class SubmittedState(DrugState):
    def proceed_to_next(self, drug_application) -> None:
        print("Proceeding from Submitted to Clinical Trial...")
        drug_application.set_state(ClinicalTrialState())

    def get_state_name(self) -> str:
        return "Submitted"

# Clinical Trial State
class ClinicalTrialState(DrugState):
    def proceed_to_next(self, drug_application) -> None:
        print("Proceeding from Clinical Trial to Under Review...")
        drug_application.set_state(UnderReviewState())

    def get_state_name(self) -> str:
        return "Clinical Trial"

# Under Review State
class UnderReviewState(DrugState):
    def proceed_to_next(self, drug_application) -> None:
        print("Proceeding from Under Review to Approved...")
        drug_application.set_state(ApprovedState())

    def get_state_name(self) -> str:
        return "Under Review"

# Approved State
class ApprovedState(DrugState):
    def proceed_to_next(self, drug_application) -> None:
        print("The drug has already been approved. No further states.")

    def get_state_name(self) -> str:
        return "Approved"

# Context class
class DrugApplication:
    def __init__(self, state: DrugState) -> None:
        self._state = state

    def set_state(self, new_state: DrugState) -> None:
        self._state = new_state
        print(f"DrugApplication: State changed to: {self._state.get_state_name()}")

    def proceed(self) -> None:
        self._state.proceed_to_next(self)

    def get_current_state(self) -> str:
        return self._state.get_state_name()

# Initial drug application in "Submitted" state
drug_application = DrugApplication(SubmittedState())

drug_application.proceed()  # Moves to Clinical Trial
drug_application.proceed()  # Moves to Under Review
drug_application.proceed()  # Moves to Approved
drug_application.proceed()  # Already Approved, no further state

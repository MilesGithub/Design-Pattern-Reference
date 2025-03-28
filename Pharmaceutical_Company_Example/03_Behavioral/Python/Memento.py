# Memento
class DrugApplicationMemento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state

# Originator
class DrugApplication:
    def __init__(self):
        self._state = ""

    def set_state(self, new_state: str) -> None:
        self._state = new_state
        print(f"DrugApplication: State has changed to: {self._state}")

    def create_memento(self) -> DrugApplicationMemento:
        return DrugApplicationMemento(self._state)

    def restore_memento(self, memento: DrugApplicationMemento) -> None:
        self._state = memento.get_state()
        print(f"DrugApplication: State restored to: {self._state}")

# Caretaker
class ApplicationCaretaker:
    def __init__(self):
        self._mementos = []

    def save_memento(self, memento: DrugApplicationMemento) -> None:
        self._mementos.append(memento)
        print("ApplicationCaretaker: Saved state.")

    def get_memento(self, index: int) -> DrugApplicationMemento:
        if 0 <= index < len(self._mementos):
            return self._mementos[index]
        else:
            raise IndexError("Invalid index for memento retrieval.")

# Create the DrugApplication and ApplicationCaretaker instances
drug_application = DrugApplication()
caretaker = ApplicationCaretaker()

# Set initial state
drug_application.set_state("Submitted")
caretaker.save_memento(drug_application.create_memento())

# Change state to clinical trial and save
drug_application.set_state("Clinical Trial")
caretaker.save_memento(drug_application.create_memento())

# Change state to review and save
drug_application.set_state("Under Review")
caretaker.save_memento(drug_application.create_memento())

# Change state to approved
drug_application.set_state("Approved")

# Restore to previous state: Under Review
drug_application.restore_memento(caretaker.get_memento(2))

# Restore to an earlier state: Clinical Trial
drug_application.restore_memento(caretaker.get_memento(1))

# Restore to the initial state: Submitted
drug_application.restore_memento(caretaker.get_memento(0))

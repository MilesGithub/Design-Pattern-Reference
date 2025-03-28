// Memento
class DrugApplicationMemento {
  constructor(state) {
    this._state = state;
  }

  getState() {
    return this._state;
  }
}

// Originator
class DrugApplication {
  constructor() {
    this._state = "";
  }

  setState(newState) {
    this._state = newState;
    console.log(`DrugApplication: State has changed to: ${this._state}`);
  }

  createMemento() {
    return new DrugApplicationMemento(this._state);
  }

  restoreMemento(memento) {
    this._state = memento.getState();
    console.log(`DrugApplication: State restored to: ${this._state}`);
  }
}

// Caretaker
class ApplicationCaretaker {
  constructor() {
    this._mementos = [];
  }

  saveMemento(memento) {
    this._mementos.push(memento);
    console.log("ApplicationCaretaker: Saved state.");
  }

  getMemento(index) {
    if (index >= 0 && index < this._mementos.length) {
      return this._mementos[index];
    } else {
      throw new Error("Invalid index for memento retrieval.");
    }
  }
}

// Create the DrugApplication and ApplicationCaretaker instances
const drugApplication = new DrugApplication();
const caretaker = new ApplicationCaretaker();

// Set initial state
drugApplication.setState("Submitted");
caretaker.saveMemento(drugApplication.createMemento());

// Change state to clinical trial and save
drugApplication.setState("Clinical Trial");
caretaker.saveMemento(drugApplication.createMemento());

// Change state to review and save
drugApplication.setState("Under Review");
caretaker.saveMemento(drugApplication.createMemento());

// Change state to approved
drugApplication.setState("Approved");

// Restore to previous state: Under Review
drugApplication.restoreMemento(caretaker.getMemento(2));

// Restore to an earlier state: Clinical Trial
drugApplication.restoreMemento(caretaker.getMemento(1));

// Restore to the initial state: Submitted
drugApplication.restoreMemento(caretaker.getMemento(0));

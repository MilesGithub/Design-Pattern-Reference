// Memento
class DrugApplicationMemento {
    private String state;

    public DrugApplicationMemento(String state) {
        this.state = state;
    }

    public String getState() {
        return state;
    }
}

// Originator
class DrugApplication {
    private String state;

    public DrugApplication() {
        this.state = "";
    }

    public void setState(String newState) {
        this.state = newState;
        System.out.println("DrugApplication: State has changed to: " + this.state);
    }

    public DrugApplicationMemento createMemento() {
        return new DrugApplicationMemento(this.state);
    }

    public void restoreMemento(DrugApplicationMemento memento) {
        this.state = memento.getState();
        System.out.println("DrugApplication: State restored to: " + this.state);
    }
}

// Caretaker
class ApplicationCaretaker {
    private List<DrugApplicationMemento> mementos;

    public ApplicationCaretaker() {
        this.mementos = new ArrayList<>();
    }

    public void saveMemento(DrugApplicationMemento memento) {
        this.mementos.add(memento);
        System.out.println("ApplicationCaretaker: Saved state.");
    }

    public DrugApplicationMemento getMemento(int index) {
        if (index >= 0 && index < mementos.size()) {
            return mementos.get(index);
        } else {
            throw new IndexOutOfBoundsException("Invalid index for memento retrieval.");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        // Create the DrugApplication and ApplicationCaretaker instances
        DrugApplication drugApplication = new DrugApplication();
        ApplicationCaretaker caretaker = new ApplicationCaretaker();

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
    }
}

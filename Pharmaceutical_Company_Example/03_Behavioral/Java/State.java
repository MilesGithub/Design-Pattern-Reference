// State interface
interface DrugState {
    void proceedToNext(DrugApplication drugApplication);
    String getStateName();
}

// Submitted State
class SubmittedState implements DrugState {
    @Override
    public void proceedToNext(DrugApplication drugApplication) {
        System.out.println("Proceeding from Submitted to Clinical Trial...");
        drugApplication.setState(new ClinicalTrialState());
    }

    @Override
    public String getStateName() {
        return "Submitted";
    }
}

// Clinical Trial State
class ClinicalTrialState implements DrugState {
    @Override
    public void proceedToNext(DrugApplication drugApplication) {
        System.out.println("Proceeding from Clinical Trial to Under Review...");
        drugApplication.setState(new UnderReviewState());
    }

    @Override
    public String getStateName() {
        return "Clinical Trial";
    }
}

// Under Review State
class UnderReviewState implements DrugState {
    @Override
    public void proceedToNext(DrugApplication drugApplication) {
        System.out.println("Proceeding from Under Review to Approved...");
        drugApplication.setState(new ApprovedState());
    }

    @Override
    public String getStateName() {
        return "Under Review";
    }
}

// Approved State
class ApprovedState implements DrugState {
    @Override
    public void proceedToNext(DrugApplication drugApplication) {
        System.out.println("The drug has already been approved. No further states.");
    }

    @Override
    public String getStateName() {
        return "Approved";
    }
}

// Context class
class DrugApplication {
    private DrugState state;

    public DrugApplication(DrugState state) {
        this.state = state;
        System.out.println("DrugApplication: Initial state -> " + state.getStateName());
    }

    public void setState(DrugState newState) {
        this.state = newState;
        System.out.println("DrugApplication: State changed to: " + state.getStateName());
    }

    public void proceed() {
        state.proceedToNext(this);
    }

    public String getCurrentState() {
        return state.getStateName();
    }
}

// Main class to test the State pattern
public class Main {
    public static void main(String[] args) {
        // Initial drug application in "Submitted" state
        DrugApplication drugApplication = new DrugApplication(new SubmittedState());

        drugApplication.proceed();  // Moves to Clinical Trial
        drugApplication.proceed();  // Moves to Under Review
        drugApplication.proceed();  // Moves to Approved
        drugApplication.proceed();  // Already Approved, no further state
    }
}

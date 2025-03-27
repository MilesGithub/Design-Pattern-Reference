// State Interface
class DrugState {
  proceedToNext(drugApplication) {
    throw new Error("This method should be overridden by concrete states!");
  }

  getStateName() {
    throw new Error("This method should be overridden by concrete states!");
  }
}

// Submitted State
class SubmittedState extends DrugState {
  proceedToNext(drugApplication) {
    console.log("Proceeding from Submitted to Clinical Trial...");
    drugApplication.setState(new ClinicalTrialState());
  }

  getStateName() {
    return "Submitted";
  }
}

// Clinical Trial State
class ClinicalTrialState extends DrugState {
  proceedToNext(drugApplication) {
    console.log("Proceeding from Clinical Trial to Under Review...");
    drugApplication.setState(new UnderReviewState());
  }

  getStateName() {
    return "Clinical Trial";
  }
}

// Under Review State
class UnderReviewState extends DrugState {
  proceedToNext(drugApplication) {
    console.log("Proceeding from Under Review to Approved...");
    drugApplication.setState(new ApprovedState());
  }

  getStateName() {
    return "Under Review";
  }
}

// Approved State
class ApprovedState extends DrugState {
  proceedToNext(drugApplication) {
    console.log("The drug has already been approved. No further states.");
  }

  getStateName() {
    return "Approved";
  }
}

// Context class
class DrugApplication {
  constructor(state) {
    this._state = state;
  }

  setState(newState) {
    this._state = newState;
    console.log(`DrugApplication: State changed to: ${this._state.getStateName()}`);
  }

  proceed() {
    this._state.proceedToNext(this);
  }

  getCurrentState() {
    return this._state.getStateName();
  }
}

// Initial drug application in "Submitted" state
const drugApplication = new DrugApplication(new SubmittedState());

drugApplication.proceed();  // Moves to Clinical Trial
drugApplication.proceed();  // Moves to Under Review
drugApplication.proceed();  // Moves to Approved
drugApplication.proceed();  // Already Approved, no further state

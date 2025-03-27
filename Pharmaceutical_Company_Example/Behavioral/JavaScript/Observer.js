// Observer Interface
class Observer {
  update(state) {
    throw new Error("This method should be overridden by concrete observers!");
  }
}

// Subject
class DrugApprovalProcess {
  constructor() {
    this._observers = [];
    this._state = "";
  }

  attachObserver(observer) {
    this._observers.push(observer);
  }

  detachObserver(observer) {
    this._observers = this._observers.filter(obs => obs !== observer);
  }

  notifyObservers() {
    console.log(`DrugApprovalProcess: Notifying observers about state change to: ${this._state}`);
    for (const observer of this._observers) {
      observer.update(this._state);
    }
  }

  setState(newState) {
    this._state = newState;
    console.log(`DrugApprovalProcess: State changed to: ${this._state}`);
    this.notifyObservers();
  }
}

// Concrete Observer: Clinical Trials Department
class ClinicalTrials extends Observer {
  update(state) {
    console.log(`Clinical Trials Department: Notified about state change to: ${state}`);
  }
}

// Concrete Observer: Quality Assurance Department
class QualityAssurance extends Observer {
  update(state) {
    console.log(`Quality Assurance Department: Notified about state change to: ${state}`);
  }
}

// Concrete Observer: Legal Department
class LegalDepartment extends Observer {
  update(state) {
    console.log(`Legal Department: Notified about state change to: ${state}`);
  }
}

// Concrete Observer: Regulatory Affairs Department
class RegulatoryAffairs extends Observer {
  update(state) {
    console.log(`Regulatory Affairs Department: Notified about state change to: ${state}`);
  }
}

// Create the DrugApprovalProcess (Subject)
const drugApprovalProcess = new DrugApprovalProcess();

// Create observers
const clinicalTrials = new ClinicalTrials();
const qualityAssurance = new QualityAssurance();
const legal = new LegalDepartment();
const regulatoryAffairs = new RegulatoryAffairs();

// Attach observers to the subject
drugApprovalProcess.attachObserver(clinicalTrials);
drugApprovalProcess.attachObserver(qualityAssurance);
drugApprovalProcess.attachObserver(legal);
drugApprovalProcess.attachObserver(regulatoryAffairs);

// Simulate state changes and notify observers
drugApprovalProcess.setState("Clinical Trial Started");
drugApprovalProcess.setState("Clinical Trial Completed");
drugApprovalProcess.setState("Quality Check in Progress");
drugApprovalProcess.setState("Under Regulatory Review");
drugApprovalProcess.setState("Approved");

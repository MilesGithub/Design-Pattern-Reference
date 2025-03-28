// Mediator Interface
class Mediator {
  notify(sender, event) {
    throw new Error("This method should be overridden by concrete mediators!");
  }
}

// Concrete Mediator
class RegulatoryMediator extends Mediator {
  constructor() {
    super();
    this.clinicalTrials = null;
    this.qualityAssurance = null;
    this.regulatoryAffairs = null;
    this.legal = null;
  }

  notify(sender, event) {
    if (event === "Clinical Trial Completed") {
      console.log("Mediator: Clinical Trial completed. Notifying Quality Assurance.");
      if (this.qualityAssurance) {
        this.qualityAssurance.checkQuality();
      }
    } else if (event === "Quality Check Completed") {
      console.log("Mediator: Quality Check completed. Notifying Regulatory Affairs.");
      if (this.regulatoryAffairs) {
        this.regulatoryAffairs.prepareDocuments();
      }
    } else if (event === "Documents Prepared") {
      console.log("Mediator: Documents prepared. Notifying Legal Department.");
      if (this.legal) {
        this.legal.reviewDocuments();
      }
    } else if (event === "Legal Review Completed") {
      console.log("Mediator: Legal Review completed. Drug is ready for final approval.");
    }
  }
}

// Department Interfaces
class Department {
  constructor(mediator) {
    this.mediator = mediator;
  }

  completeTask() {
    throw new Error("This method should be overridden by concrete departments!");
  }
}

// Concrete Department: Clinical Trials
class ClinicalTrials extends Department {
  runTrials() {
    console.log("Clinical Trials: Running clinical trials...");
    this.mediator.notify("ClinicalTrials", "Clinical Trial Completed");
  }
}

// Concrete Department: Quality Assurance
class QualityAssurance extends Department {
  checkQuality() {
    console.log("Quality Assurance: Checking product quality...");
    this.mediator.notify("QualityAssurance", "Quality Check Completed");
  }
}

// Concrete Department: Regulatory Affairs
class RegulatoryAffairs extends Department {
  prepareDocuments() {
    console.log("Regulatory Affairs: Preparing regulatory documents...");
    this.mediator.notify("RegulatoryAffairs", "Documents Prepared");
  }
}

// Concrete Department: Legal Department
class LegalDepartment extends Department {
  reviewDocuments() {
    console.log("Legal Department: Reviewing regulatory documents...");
    this.mediator.notify("LegalDepartment", "Legal Review Completed");
  }
}

// Create the Mediator
const mediator = new RegulatoryMediator();

// Create Departments
const clinicalTrials = new ClinicalTrials(mediator);
const qualityAssurance = new QualityAssurance(mediator);
const regulatoryAffairs = new RegulatoryAffairs(mediator);
const legal = new LegalDepartment(mediator);

// Set Departments in the Mediator
mediator.clinicalTrials = clinicalTrials;
mediator.qualityAssurance = qualityAssurance;
mediator.regulatoryAffairs = regulatoryAffairs;
mediator.legal = legal;

// Run process
clinicalTrials.runTrials();

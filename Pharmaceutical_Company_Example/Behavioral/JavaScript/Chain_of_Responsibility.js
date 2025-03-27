// Base class for a drug approval request handler
class DrugApprovalHandler {
  constructor() {
    this.nextHandler = null;
  }

  setNext(handler) {
    this.nextHandler = handler;
    return handler;
  }

  handleRequest(drug) {
    throw new Error("This method should be implemented by subclasses.");
  }

  passToNext(drug) {
    if (this.nextHandler) {
      this.nextHandler.handleRequest(drug);
    } else {
      console.log("End of chain, no handler could process the request.");
    }
  }
}

// Concrete handler for Initial Review
class InitialReviewHandler extends DrugApprovalHandler {
  handleRequest(drug) {
    if (drug.initial_review_status === "Pending") {
      console.log(`Initial review passed for ${drug.name}`);
      drug.initial_review_status = "Approved";
      this.passToNext(drug);
    } else {
      console.log(`Initial review already processed for ${drug.name}`);
      this.passToNext(drug);
    }
  }
}

// Concrete handler for Clinical Trials Review
class ClinicalTrialsHandler extends DrugApprovalHandler {
  handleRequest(drug) {
    if (drug.clinical_trials_status === "Pending") {
      console.log(`Clinical trials review passed for ${drug.name}`);
      drug.clinical_trials_status = "Approved";
      this.passToNext(drug);
    } else {
      console.log(`Clinical trials already processed for ${drug.name}`);
      this.passToNext(drug);
    }
  }
}

// Concrete handler for Regulatory Review
class RegulatoryReviewHandler extends DrugApprovalHandler {
  handleRequest(drug) {
    if (drug.regulatory_status === "Pending") {
      console.log(`Regulatory review passed for ${drug.name}`);
      drug.regulatory_status = "Approved";
      this.passToNext(drug);
    } else {
      console.log(`Regulatory review already processed for ${drug.name}`);
      this.passToNext(drug);
    }
  }
}

// Concrete handler for Final Approval
class FinalApprovalHandler extends DrugApprovalHandler {
  handleRequest(drug) {
    if (
      drug.initial_review_status === "Approved" &&
      drug.clinical_trials_status === "Approved" &&
      drug.regulatory_status === "Approved"
    ) {
      console.log(`Final approval granted for ${drug.name}`);
      drug.final_approval_status = "Approved";
    } else {
      console.log(`Drug ${drug.name} could not pass final approval.`);
    }
  }
}

let drug1 = {
  name: "Test Small Molecule 01",
  initial_review_status: "Pending",
  clinical_trials_status: "Pending",
  regulatory_status: "Pending",
  final_approval_status: "Pending",
};

// Setup the chain of responsibility
const initialReview = new InitialReviewHandler();
const clinicalTrials = new ClinicalTrialsHandler();
const regulatoryReview = new RegulatoryReviewHandler();
const finalApproval = new FinalApprovalHandler();

initialReview.setNext(clinicalTrials).setNext(regulatoryReview).setNext(finalApproval);

initialReview.handleRequest(drug1);

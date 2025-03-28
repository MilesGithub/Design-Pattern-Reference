#include <iostream>
#include <string>

using namespace std;

// Struct to hold drug information
struct Drug {
  string name;
  string initial_review_status;
  string clinical_trials_status;
  string regulatory_status;
  string final_approval_status;
};

// Base class for a drug approval request handler
class DrugApprovalHandler {
protected:
  DrugApprovalHandler* nextHandler;
  
public:
  DrugApprovalHandler() : nextHandler(nullptr) {}
  
  void setNext(DrugApprovalHandler* handler) {
    nextHandler = handler;
  }
  
  virtual void handleRequest(Drug& drug) = 0;
  
protected:
  void passToNext(Drug& drug) {
    if (nextHandler) {
      nextHandler->handleRequest(drug);
    } else {
      cout << "End of chain, no handler could process the request." << endl;
    }
  }
};

// Concrete handler for Initial Review
class InitialReviewHandler : public DrugApprovalHandler {
public:
  void handleRequest(Drug& drug) override {
    if (drug.initial_review_status == "Pending") {
      cout << "Initial review passed for " << drug.name << endl;
      drug.initial_review_status = "Approved";
      passToNext(drug);
    } else {
      cout << "Initial review already processed for " << drug.name << endl;
      passToNext(drug);
    }
  }
};

// Concrete handler for Clinical Trials Review
class ClinicalTrialsHandler : public DrugApprovalHandler {
public:
  void handleRequest(Drug& drug) override {
    if (drug.clinical_trials_status == "Pending") {
      cout << "Clinical trials review passed for " << drug.name << endl;
      drug.clinical_trials_status = "Approved";
      passToNext(drug);
    } else {
      cout << "Clinical trials already processed for " << drug.name << endl;
      passToNext(drug);
    }
  }
};

// Concrete handler for Regulatory Review
class RegulatoryReviewHandler : public DrugApprovalHandler {
public:
  void handleRequest(Drug& drug) override {
    if (drug.regulatory_status == "Pending") {
      cout << "Regulatory review passed for " << drug.name << endl;
      drug.regulatory_status = "Approved";
      passToNext(drug);
    } else {
      cout << "Regulatory review already processed for " << drug.name << endl;
      passToNext(drug);
    }
  }
};

// Concrete handler for Final Approval
class FinalApprovalHandler : public DrugApprovalHandler {
public:
  void handleRequest(Drug& drug) override {
    if (drug.initial_review_status == "Approved" &&
        drug.clinical_trials_status == "Approved" &&
        drug.regulatory_status == "Approved") {
      cout << "Final approval granted for " << drug.name << endl;
      drug.final_approval_status = "Approved";
    } else {
      cout << "Drug " << drug.name << " could not pass final approval." << endl;
    }
  }
};

int main() {
  Drug drug1 = {
    "Test Small Molecule 01",
    "Pending",
    "Pending",
    "Pending",
    "Pending"
  };
  
  // Setup the chain of responsibility
  InitialReviewHandler initialReview;
  ClinicalTrialsHandler clinicalTrials;
  RegulatoryReviewHandler regulatoryReview;
  FinalApprovalHandler finalApproval;
  
  initialReview.setNext(&clinicalTrials);
  clinicalTrials.setNext(&regulatoryReview);
  regulatoryReview.setNext(&finalApproval);
  
  // Start processing
  initialReview.handleRequest(drug1);
  
  return 0;
}

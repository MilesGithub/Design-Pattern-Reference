#include <iostream>
#include <string>

// Subsystem 1: Clinical Trials
class ClinicalTrials {
public:
  void submitTrialData(const std::string& drugName) {
    std::cout << drugName << " clinical trial data submitted." << std::endl;
  }
  
  void reviewTrialData(const std::string& drugName) {
    std::cout << drugName << " clinical trial data reviewed and approved." << std::endl;
  }
};

// Subsystem 2: Safety Review
class SafetyReview {
public:
  void submitSafetyData(const std::string& drugName) {
    std::cout << drugName << " safety data submitted." << std::endl;
  }
  
  void reviewSafetyData(const std::string& drugName) {
    std::cout << drugName << " safety data reviewed and approved." << std::endl;
  }
};

// Subsystem 3: Regulatory Compliance
class RegulatoryCompliance {
public:
  void submitRegulatoryDocuments(const std::string& drugName) {
    std::cout << drugName << " regulatory documents submitted." << std::endl;
  }
  
  void obtainApproval(const std::string& drugName) {
    std::cout << drugName << " regulatory approval granted." << std::endl;
  }
};

// Facade class to simplify interactions with subsystems
class DrugApprovalFacade {
public:
  DrugApprovalFacade() {
    clinicalTrials = new ClinicalTrials();
    safetyReview = new SafetyReview();
    regulatoryCompliance = new RegulatoryCompliance();
  }
  
  void submitForApproval(const std::string& drugName) {
    std::cout << "Starting approval process for " << drugName << "...\n" << std::endl;
    
    clinicalTrials->submitTrialData(drugName);
    clinicalTrials->reviewTrialData(drugName);
    
    safetyReview->submitSafetyData(drugName);
    safetyReview->reviewSafetyData(drugName);
    
    regulatoryCompliance->submitRegulatoryDocuments(drugName);
    regulatoryCompliance->obtainApproval(drugName);
    
    std::cout << "\n" << drugName << " has been approved.\n" << std::endl;
  }
  
private:
  ClinicalTrials* clinicalTrials;
  SafetyReview* safetyReview;
  RegulatoryCompliance* regulatoryCompliance;
};

int main() {
  DrugApprovalFacade drugFacade;
  
  drugFacade.submitForApproval("Test Small Molecule 01");
  drugFacade.submitForApproval("Test Small Molecule 02");
  drugFacade.submitForApproval("Test Small Molecule 03");
  
  return 0;
}

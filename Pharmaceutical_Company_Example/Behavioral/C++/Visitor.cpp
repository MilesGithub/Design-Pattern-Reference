#include <iostream>
#include <string>

// Forward declaration of Visitor
class Visitor;

// Element Interface for Regulatory Steps
class RegulatoryStep {
public:
  virtual void accept(Visitor& visitor) = 0;
  virtual ~RegulatoryStep() = default;
};

// Concrete Elements
class DocumentationSubmission : public RegulatoryStep {
public:
  void accept(Visitor& visitor) override;
};

class ClinicalTrialReview : public RegulatoryStep {
public:
  void accept(Visitor& visitor) override;
};

class SafetyEvaluation : public RegulatoryStep {
public:
  void accept(Visitor& visitor) override;
};

// Visitor Interface
class Visitor {
public:
  virtual void visit_documentation_submission(DocumentationSubmission& documentation) = 0;
  virtual void visit_clinical_trial_review(ClinicalTrialReview& trial_review) = 0;
  virtual void visit_safety_evaluation(SafetyEvaluation& safety_evaluation) = 0;
  virtual ~Visitor() = default;
};

// Concrete Visitor Auditor
class Auditor : public Visitor {
public:
  void visit_documentation_submission(DocumentationSubmission& documentation) override {
    std::cout << "Auditing documentation submission..." << std::endl;
  }
  
  void visit_clinical_trial_review(ClinicalTrialReview& trial_review) override {
    std::cout << "Auditing clinical trial review process..." << std::endl;
  }
  
  void visit_safety_evaluation(SafetyEvaluation& safety_evaluation) override {
    std::cout << "Auditing safety evaluation..." << std::endl;
  }
};

// Concrete Visitor Report Generator
class ReportGenerator : public Visitor {
public:
  void visit_documentation_submission(DocumentationSubmission& documentation) override {
    std::cout << "Generating report for documentation submission..." << std::endl;
  }
  
  void visit_clinical_trial_review(ClinicalTrialReview& trial_review) override {
    std::cout << "Generating report for clinical trial review..." << std::endl;
  }
  
  void visit_safety_evaluation(SafetyEvaluation& safety_evaluation) override {
    std::cout << "Generating report for safety evaluation..." << std::endl;
  }
};

// Concrete Visitor Approval Checker
class ApprovalChecker : public Visitor {
public:
  void visit_documentation_submission(DocumentationSubmission& documentation) override {
    std::cout << "Checking approval status of documentation submission..." << std::endl;
  }
  
  void visit_clinical_trial_review(ClinicalTrialReview& trial_review) override {
    std::cout << "Checking approval status of clinical trial review..." << std::endl;
  }
  
  void visit_safety_evaluation(SafetyEvaluation& safety_evaluation) override {
    std::cout << "Checking approval status of safety evaluation..." << std::endl;
  }
};

// Define accept functions for elements
void DocumentationSubmission::accept(Visitor& visitor) {
  visitor.visit_documentation_submission(*this);
}

void ClinicalTrialReview::accept(Visitor& visitor) {
  visitor.visit_clinical_trial_review(*this);
}

void SafetyEvaluation::accept(Visitor& visitor) {
  visitor.visit_safety_evaluation(*this);
}

int main() {
  // Define regulatory steps
  DocumentationSubmission documentation;
  ClinicalTrialReview clinical_trials;
  SafetyEvaluation safety_eval;
  
  // Define visitors
  Auditor auditor;
  ReportGenerator report_generator;
  ApprovalChecker approval_checker;
  
  // Use the Auditor visitor on different steps
  documentation.accept(auditor);
  clinical_trials.accept(auditor);
  safety_eval.accept(auditor);
  
  // Use the Report Generator visitor on different steps
  documentation.accept(report_generator);
  clinical_trials.accept(report_generator);
  safety_eval.accept(report_generator);
  
  // Use the Approval Checker visitor on different steps
  documentation.accept(approval_checker);
  clinical_trials.accept(approval_checker);
  safety_eval.accept(approval_checker);
  
  return 0;
}

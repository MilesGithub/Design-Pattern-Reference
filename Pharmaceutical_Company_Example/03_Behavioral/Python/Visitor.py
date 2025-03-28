from abc import ABC, abstractmethod

# Define Element Interface for Regulatory Steps
class RegulatoryStep(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Concrete Elements
class DocumentationSubmission(RegulatoryStep):
    def accept(self, visitor):
        visitor.visit_documentation_submission(self)

class ClinicalTrialReview(RegulatoryStep):
    def accept(self, visitor):
        visitor.visit_clinical_trial_review(self)

class SafetyEvaluation(RegulatoryStep):
    def accept(self, visitor):
        visitor.visit_safety_evaluation(self)

# Visitor Interface
class Visitor(ABC):
    @abstractmethod
    def visit_documentation_submission(self, documentation):
        pass

    @abstractmethod
    def visit_clinical_trial_review(self, trial_review):
        pass

    @abstractmethod
    def visit_safety_evaluation(self, safety_evaluation):
        pass

# Concrete Visitor Auditor
class Auditor(Visitor):
    def visit_documentation_submission(self, documentation):
        print("Auditing documentation submission...")

    def visit_clinical_trial_review(self, trial_review):
        print("Auditing clinical trial review process...")

    def visit_safety_evaluation(self, safety_evaluation):
        print("Auditing safety evaluation...")

# Concrete Visitor Report Generator
class ReportGenerator(Visitor):
    def visit_documentation_submission(self, documentation):
        print("Generating report for documentation submission...")

    def visit_clinical_trial_review(self, trial_review):
        print("Generating report for clinical trial review...")

    def visit_safety_evaluation(self, safety_evaluation):
        print("Generating report for safety evaluation...")

# Concrete Visitor Approval Checker
class ApprovalChecker(Visitor):
    def visit_documentation_submission(self, documentation):
        print("Checking approval status of documentation submission...")

    def visit_clinical_trial_review(self, trial_review):
        print("Checking approval status of clinical trial review...")

    def visit_safety_evaluation(self, safety_evaluation):
        print("Checking approval status of safety evaluation...")

# Define the regulatory steps
documentation = DocumentationSubmission()
clinical_trials = ClinicalTrialReview()
safety_eval = SafetyEvaluation()

# Define visitors
auditor = Auditor()
report_generator = ReportGenerator()
approval_checker = ApprovalChecker()

# Use the Auditor visitor on different steps
documentation.accept(auditor)
clinical_trials.accept(auditor)
safety_eval.accept(auditor)

# Use the Report Generator visitor on different steps
documentation.accept(report_generator)
clinical_trials.accept(report_generator)
safety_eval.accept(report_generator)

# Use the Approval Checker visitor on different steps
documentation.accept(approval_checker)
clinical_trials.accept(approval_checker)
safety_eval.accept(approval_checker)

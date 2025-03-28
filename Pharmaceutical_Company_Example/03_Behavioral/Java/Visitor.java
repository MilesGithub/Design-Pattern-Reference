// Define Element Interface for Regulatory Steps
interface RegulatoryStep {
    void accept(Visitor visitor);
}

// Concrete Elements
class DocumentationSubmission implements RegulatoryStep {
    public void accept(Visitor visitor) {
        visitor.visitDocumentationSubmission(this);
    }
}

class ClinicalTrialReview implements RegulatoryStep {
    public void accept(Visitor visitor) {
        visitor.visitClinicalTrialReview(this);
    }
}

class SafetyEvaluation implements RegulatoryStep {
    public void accept(Visitor visitor) {
        visitor.visitSafetyEvaluation(this);
    }
}

// Visitor Interface
interface Visitor {
    void visitDocumentationSubmission(DocumentationSubmission documentation);
    void visitClinicalTrialReview(ClinicalTrialReview trialReview);
    void visitSafetyEvaluation(SafetyEvaluation safetyEvaluation);
}

// Concrete Visitor: Auditor
class Auditor implements Visitor {
    public void visitDocumentationSubmission(DocumentationSubmission documentation) {
        System.out.println("Auditing documentation submission...");
    }

    public void visitClinicalTrialReview(ClinicalTrialReview trialReview) {
        System.out.println("Auditing clinical trial review process...");
    }

    public void visitSafetyEvaluation(SafetyEvaluation safetyEvaluation) {
        System.out.println("Auditing safety evaluation...");
    }
}

// Concrete Visitor: Report Generator
class ReportGenerator implements Visitor {
    public void visitDocumentationSubmission(DocumentationSubmission documentation) {
        System.out.println("Generating report for documentation submission...");
    }

    public void visitClinicalTrialReview(ClinicalTrialReview trialReview) {
        System.out.println("Generating report for clinical trial review...");
    }

    public void visitSafetyEvaluation(SafetyEvaluation safetyEvaluation) {
        System.out.println("Generating report for safety evaluation...");
    }
}

// Concrete Visitor: Approval Checker
class ApprovalChecker implements Visitor {
    public void visitDocumentationSubmission(DocumentationSubmission documentation) {
        System.out.println("Checking approval status of documentation submission...");
    }

    public void visitClinicalTrialReview(ClinicalTrialReview trialReview) {
        System.out.println("Checking approval status of clinical trial review...");
    }

    public void visitSafetyEvaluation(SafetyEvaluation safetyEvaluation) {
        System.out.println("Checking approval status of safety evaluation...");
    }
}

// Main class to execute the Visitor pattern
public class Main {
    public static void main(String[] args) {
        // Define regulatory steps
        RegulatoryStep documentation = new DocumentationSubmission();
        RegulatoryStep clinicalTrials = new ClinicalTrialReview();
        RegulatoryStep safetyEval = new SafetyEvaluation();

        // Define visitors
        Visitor auditor = new Auditor();
        Visitor reportGenerator = new ReportGenerator();
        Visitor approvalChecker = new ApprovalChecker();

        // Apply the Auditor visitor to different steps
        documentation.accept(auditor);
        clinicalTrials.accept(auditor);
        safetyEval.accept(auditor);

        System.out.println();

        // Apply the Report Generator visitor to different steps
        documentation.accept(reportGenerator);
        clinicalTrials.accept(reportGenerator);
        safetyEval.accept(reportGenerator);

        System.out.println();

        // Apply the Approval Checker visitor to different steps
        documentation.accept(approvalChecker);
        clinicalTrials.accept(approvalChecker);
        safetyEval.accept(approvalChecker);
    }
}

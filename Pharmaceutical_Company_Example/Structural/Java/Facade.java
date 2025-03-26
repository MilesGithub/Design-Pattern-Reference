// Subsystem 1: Clinical Trials
class ClinicalTrials {
    public void submitTrialData(String drugName) {
        System.out.println(drugName + " clinical trial data submitted.");
    }

    public void reviewTrialData(String drugName) {
        System.out.println(drugName + " clinical trial data reviewed and approved.");
    }
}

// Subsystem 2: Safety Review
class SafetyReview {
    public void submitSafetyData(String drugName) {
        System.out.println(drugName + " safety data submitted.");
    }

    public void reviewSafetyData(String drugName) {
        System.out.println(drugName + " safety data reviewed and approved.");
    }
}

// Subsystem 3: Regulatory Compliance
class RegulatoryCompliance {
    public void submitRegulatoryDocuments(String drugName) {
        System.out.println(drugName + " regulatory documents submitted.");
    }

    public void obtainApproval(String drugName) {
        System.out.println(drugName + " regulatory approval granted.");
    }
}

// Facade class to simplify interactions with subsystems
class DrugApprovalFacade {
    private ClinicalTrials clinicalTrials;
    private SafetyReview safetyReview;
    private RegulatoryCompliance regulatoryCompliance;

    public DrugApprovalFacade() {
        clinicalTrials = new ClinicalTrials();
        safetyReview = new SafetyReview();
        regulatoryCompliance = new RegulatoryCompliance();
    }

    public void submitForApproval(String drugName) {
        System.out.println("Starting approval process for " + drugName + "...\n");

        clinicalTrials.submitTrialData(drugName);
        clinicalTrials.reviewTrialData(drugName);

        safetyReview.submitSafetyData(drugName);
        safetyReview.reviewSafetyData(drugName);

        regulatoryCompliance.submitRegulatoryDocuments(drugName);
        regulatoryCompliance.obtainApproval(drugName);

        System.out.println("\n" + drugName + " has been approved.\n");
    }
}

// Main class to test the facade implementation
public class DrugApprovalFacadeExample {
    public static void main(String[] args) {
        DrugApprovalFacade drugFacade = new DrugApprovalFacade();

        drugFacade.submitForApproval("Test Small Molecule 01");
        drugFacade.submitForApproval("Test Small Molecule 02");
        drugFacade.submitForApproval("Test Small Molecule 03");
    }
}

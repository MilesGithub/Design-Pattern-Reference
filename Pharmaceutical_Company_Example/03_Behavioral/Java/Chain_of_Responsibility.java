// Base class for a drug approval request handler
abstract class DrugApprovalHandler {
    protected DrugApprovalHandler nextHandler;

    public void setNext(DrugApprovalHandler handler) {
        this.nextHandler = handler;
    }

    public abstract void handleRequest(Drug drug);

    protected void passToNext(Drug drug) {
        if (nextHandler != null) {
            nextHandler.handleRequest(drug);
        } else {
            System.out.println("End of chain, no handler could process the request.");
        }
    }
}

// Concrete handler for Initial Review
class InitialReviewHandler extends DrugApprovalHandler {
    @Override
    public void handleRequest(Drug drug) {
        if ("Pending".equals(drug.getInitialReviewStatus())) {
            System.out.println("Initial review passed for " + drug.getName());
            drug.setInitialReviewStatus("Approved");
            passToNext(drug);
        } else {
            System.out.println("Initial review already processed for " + drug.getName());
            passToNext(drug);
        }
    }
}

// Concrete handler for Clinical Trials Review
class ClinicalTrialsHandler extends DrugApprovalHandler {
    @Override
    public void handleRequest(Drug drug) {
        if ("Pending".equals(drug.getClinicalTrialsStatus())) {
            System.out.println("Clinical trials review passed for " + drug.getName());
            drug.setClinicalTrialsStatus("Approved");
            passToNext(drug);
        } else {
            System.out.println("Clinical trials already processed for " + drug.getName());
            passToNext(drug);
        }
    }
}

// Concrete handler for Regulatory Review
class RegulatoryReviewHandler extends DrugApprovalHandler {
    @Override
    public void handleRequest(Drug drug) {
        if ("Pending".equals(drug.getRegulatoryStatus())) {
            System.out.println("Regulatory review passed for " + drug.getName());
            drug.setRegulatoryStatus("Approved");
            passToNext(drug);
        } else {
            System.out.println("Regulatory review already processed for " + drug.getName());
            passToNext(drug);
        }
    }
}

// Concrete handler for Final Approval
class FinalApprovalHandler extends DrugApprovalHandler {
    @Override
    public void handleRequest(Drug drug) {
        if ("Approved".equals(drug.getInitialReviewStatus()) &&
            "Approved".equals(drug.getClinicalTrialsStatus()) &&
            "Approved".equals(drug.getRegulatoryStatus())) {
            System.out.println("Final approval granted for " + drug.getName());
            drug.setFinalApprovalStatus("Approved");
        } else {
            System.out.println("Drug " + drug.getName() + " could not pass final approval.");
        }
    }
}

// Drug class to represent the drug details
class Drug {
    private String name;
    private String initialReviewStatus;
    private String clinicalTrialsStatus;
    private String regulatoryStatus;
    private String finalApprovalStatus;

    public Drug(String name, String initialReviewStatus, String clinicalTrialsStatus, String regulatoryStatus, String finalApprovalStatus) {
        this.name = name;
        this.initialReviewStatus = initialReviewStatus;
        this.clinicalTrialsStatus = clinicalTrialsStatus;
        this.regulatoryStatus = regulatoryStatus;
        this.finalApprovalStatus = finalApprovalStatus;
    }

    public String getName() {
        return name;
    }

    public String getInitialReviewStatus() {
        return initialReviewStatus;
    }

    public void setInitialReviewStatus(String initialReviewStatus) {
        this.initialReviewStatus = initialReviewStatus;
    }

    public String getClinicalTrialsStatus() {
        return clinicalTrialsStatus;
    }

    public void setClinicalTrialsStatus(String clinicalTrialsStatus) {
        this.clinicalTrialsStatus = clinicalTrialsStatus;
    }

    public String getRegulatoryStatus() {
        return regulatoryStatus;
    }

    public void setRegulatoryStatus(String regulatoryStatus) {
        this.regulatoryStatus = regulatoryStatus;
    }

    public String getFinalApprovalStatus() {
        return finalApprovalStatus;
    }

    public void setFinalApprovalStatus(String finalApprovalStatus) {
        this.finalApprovalStatus = finalApprovalStatus;
    }
}

public class Main {
    public static void main(String[] args) {
        // Setup the chain of responsibility
        DrugApprovalHandler initialReview = new InitialReviewHandler();
        DrugApprovalHandler clinicalTrials = new ClinicalTrialsHandler();
        DrugApprovalHandler regulatoryReview = new RegulatoryReviewHandler();
        DrugApprovalHandler finalApproval = new FinalApprovalHandler();

        initialReview.setNext(clinicalTrials);
        clinicalTrials.setNext(regulatoryReview);
        regulatoryReview.setNext(finalApproval);

        // Creating the drug object
        Drug drug1 = new Drug("Test Small Molecule 01", "Pending", "Pending", "Pending", "Pending");

        // Start the request processing
        initialReview.handleRequest(drug1);
    }
}

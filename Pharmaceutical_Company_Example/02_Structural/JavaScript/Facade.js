// Subsystem 1: Clinical Trials
class ClinicalTrials {
    submitTrialData(drugName) {
        console.log(`${drugName} clinical trial data submitted.`);
    }

    reviewTrialData(drugName) {
        console.log(`${drugName} clinical trial data reviewed and approved.`);
    }
}

// Subsystem 2: Safety Review
class SafetyReview {
    submitSafetyData(drugName) {
        console.log(`${drugName} safety data submitted.`);
    }

    reviewSafetyData(drugName) {
        console.log(`${drugName} safety data reviewed and approved.`);
    }
}

// Subsystem 3: Regulatory Compliance
class RegulatoryCompliance {
    submitRegulatoryDocuments(drugName) {
        console.log(`${drugName} regulatory documents submitted.`);
    }

    obtainApproval(drugName) {
        console.log(`${drugName} regulatory approval granted.`);
    }
}

// Facade class to simplify interactions with subsystems
class DrugApprovalFacade {
    constructor() {
        this.clinicalTrials = new ClinicalTrials();
        this.safetyReview = new SafetyReview();
        this.regulatoryCompliance = new RegulatoryCompliance();
    }

    submitForApproval(drugName) {
        console.log(`Starting approval process for ${drugName}...\n`);
        
        this.clinicalTrials.submitTrialData(drugName);
        this.clinicalTrials.reviewTrialData(drugName);
        
        this.safetyReview.submitSafetyData(drugName);
        this.safetyReview.reviewSafetyData(drugName);
        
        this.regulatoryCompliance.submitRegulatoryDocuments(drugName);
        this.regulatoryCompliance.obtainApproval(drugName);
        
        console.log(`\n${drugName} has been approved.\n`);
    }
}

// Usage
const drugFacade = new DrugApprovalFacade();

drugFacade.submitForApproval("Test Small Molecule 01");
drugFacade.submitForApproval("Test Small Molecule 02");
drugFacade.submitForApproval("Test Small Molecule 03");

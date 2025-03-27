// Adaptee: ClinicalTrialSystem
class ClinicalTrialSystem {
  constructor(drugName) {
    this.trialData = `${drugName} clinical trial data`;
  }

  getTrialData() {
    return this.trialData;
  }
}

// Target: RegulatoryAPI
class RegulatoryAPI {
  uploadDataToRegulator(data) {
    console.log(`Uploading the following data to regulatory authorities: ${data}`);
  }
}

// Adapter to bridge between ClinicalTrialSystem (Adaptee) and RegulatoryAPI (Target)
class RegulatoryAdapter {
  constructor(clinicalTrialSystem, regulatoryAPI) {
    this.clinicalTrialSystem = clinicalTrialSystem;
    this.regulatoryAPI = regulatoryAPI;
  }

  submitTrialData() {
    const trialData = this.clinicalTrialSystem.getTrialData();
    this.regulatoryAPI.uploadDataToRegulator(trialData);
  }
}

// Create instances of ClinicalTrialSystem and RegulatoryAPI
const clinicalSystem1 = new ClinicalTrialSystem("Test Small Molecule 01");
const clinicalSystem2 = new ClinicalTrialSystem("Test Small Molecule 02");
const regulatoryAPI = new RegulatoryAPI();

// Create adapters for both clinical systems
const adapter1 = new RegulatoryAdapter(clinicalSystem1, regulatoryAPI);
adapter1.submitTrialData();

const adapter2 = new RegulatoryAdapter(clinicalSystem2, regulatoryAPI);
adapter2.submitTrialData();

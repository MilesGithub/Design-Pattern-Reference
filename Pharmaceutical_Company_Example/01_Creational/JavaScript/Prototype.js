// Prototype
class RegulatoryDocumentPrototype {
  constructor(drugName, documentType, clinicalTrialData, safetyReport, manufacturingData) {
    this.drugName = drugName;
    this.documentType = documentType;
    this.clinicalTrialData = clinicalTrialData;
    this.safetyReport = safetyReport;
    this.manufacturingData = manufacturingData;
  }

  // Clone method creates a new instance with the same data but a new drug name
  cloneDocument(newDrugName) {
    return new RegulatoryDocumentPrototype(
      newDrugName,
      this.documentType,
      this.clinicalTrialData,
      this.safetyReport,
      this.manufacturingData
    );
  }

  // Show document details
  showDocument() {
    console.log(`Regulatory Document for: ${this.drugName}\n` +
      `Document Type: ${this.documentType}\n` +
      `Clinical Trial Data: ${this.clinicalTrialData}\n` +
      `Safety Report: ${this.safetyReport}\n` +
      `Manufacturing Data: ${this.manufacturingData}\n`);
  }
}

// Create prototypes
const vaccinePrototype = new RegulatoryDocumentPrototype(
  "Vaccine Prototype",
  "Vaccine Regulatory Document",
  "Standard vaccine clinical trial data",
  "Standard vaccine safety report",
  "Standard vaccine manufacturing data"
);

const smallMoleculePrototype = new RegulatoryDocumentPrototype(
  "Small-Molecule Prototype",
  "Small-Molecule Regulatory Document",
  "Standard small-molecule clinical trial data",
  "Standard small-molecule safety report",
  "Standard small-molecule manufacturing data"
);

const biologicsPrototype = new RegulatoryDocumentPrototype(
  "Biologics Prototype",
  "Biologics Regulatory Document",
  "Standard biologics clinical trial data",
  "Standard biologics safety report",
  "Standard biologics manufacturing data"
);

// Clone the vaccine prototype for a new vaccine
const newVaccineDocument = vaccinePrototype.cloneDocument("Test Vaccine 01");
newVaccineDocument.showDocument();

// Clone the small-molecule prototype for a new drug
const newSmallMoleculeDocument = smallMoleculePrototype.cloneDocument("Test Small Molecule 01");
newSmallMoleculeDocument.showDocument();

// Clone the biologics prototype for a new biologic drug
const newBiologicsDocument = biologicsPrototype.cloneDocument("Test Monoclonal Antibody 01");
newBiologicsDocument.showDocument();

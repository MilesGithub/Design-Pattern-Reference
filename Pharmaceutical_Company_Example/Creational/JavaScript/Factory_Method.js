// Product
class RegulatoryDocument {
  constructor(drugName) {
    this.drugName = drugName;
    this.clinicalTrialData = null;
    this.safetyReport = null;
    this.manufacturingData = null;
  }

  showDocument() {
    console.log(`Regulatory Document for: ${this.drugName}\n` +
      `Clinical Trial Data: ${this.clinicalTrialData}\n` +
      `Safety Report: ${this.safetyReport}\n` +
      `Manufacturing Data: ${this.manufacturingData}\n`);
  }
}

// Abstract Builder
class RegulatoryDocumentBuilder {
  constructor(drugName) {
    this.document = new RegulatoryDocument(drugName);
  }

  addClinicalTrialData() {
    throw new Error("This method must be overridden by a concrete builder");
  }

  addSafetyReport() {
    throw new Error("This method must be overridden by a concrete builder");
  }

  addManufacturingData() {
    throw new Error("This method must be overridden by a concrete builder");
  }

  getDocument() {
    return this.document;
  }
}

// Concrete Builder for Vaccines
class VaccineDocumentBuilder extends RegulatoryDocumentBuilder {
  addClinicalTrialData() {
    this.document.clinicalTrialData = "Vaccine clinical trial data";
  }

  addSafetyReport() {
    this.document.safetyReport = "Vaccine safety report";
  }

  addManufacturingData() {
    this.document.manufacturingData = "Vaccine manufacturing data";
  }
}

// Concrete Builder for Small-Molecule Drugs
class SmallMoleculeDocumentBuilder extends RegulatoryDocumentBuilder {
  addClinicalTrialData() {
    this.document.clinicalTrialData = "Small-molecule clinical trial data";
  }

  addSafetyReport() {
    this.document.safetyReport = "Small-molecule safety report";
  }

  addManufacturingData() {
    this.document.manufacturingData = "Small-molecule manufacturing data";
  }
}

// Concrete Builder for Biologics
class BiologicsDocumentBuilder extends RegulatoryDocumentBuilder {
  addClinicalTrialData() {
    this.document.clinicalTrialData = "Biologics clinical trial data";
  }

  addSafetyReport() {
    this.document.safetyReport = "Biologics safety report";
  }

  addManufacturingData() {
    this.document.manufacturingData = "Biologics manufacturing data";
  }
}

// Director: Manages the building process
class RegulatoryDirector {
  constructor(builder) {
    this.builder = builder;
  }

  constructDocument() {
    this.builder.addClinicalTrialData();
    this.builder.addSafetyReport();
    this.builder.addManufacturingData();
  }

  getDocument() {
    return this.builder.getDocument();
  }
}

// Create a director for a Vaccine regulatory document
let vaccineBuilder = new VaccineDocumentBuilder("Test Vaccine 01");
let director = new RegulatoryDirector(vaccineBuilder);
director.constructDocument();
let vaccineDoc = director.getDocument();
vaccineDoc.showDocument();

// Create a director for a Small-Molecule regulatory document
let smallMoleculeBuilder = new SmallMoleculeDocumentBuilder("Test Small Molecule 01");
director = new RegulatoryDirector(smallMoleculeBuilder);
director.constructDocument();
let smallMoleculeDoc = director.getDocument();
smallMoleculeDoc.showDocument();

// Create a director for a Biologics regulatory document
let biologicsBuilder = new BiologicsDocumentBuilder("Test Monoclonal Antibody 01");
director = new RegulatoryDirector(biologicsBuilder);
director.constructDocument();
let biologicsDoc = director.getDocument();
biologicsDoc.showDocument();

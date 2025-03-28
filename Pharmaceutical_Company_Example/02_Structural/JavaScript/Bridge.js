// Abstraction
class RegulatoryProcess {
  constructor(implementation) {
    this.implementation = implementation;
  }

  submit() {
    this.implementation.submit();
  }

  approve() {
    this.implementation.approve();
  }
}

// Concrete implementation for Vaccines
class VaccineProcess {
  submit() {
    console.log("Submitting vaccine clinical trial data...");
  }

  approve() {
    console.log("Vaccine regulatory approval granted.");
  }
}

// Concrete implementation for Small-Molecule Drugs
class SmallMoleculeDrugProcess {
  submit() {
    console.log("Submitting small-molecule clinical trial data...");
  }

  approve() {
    console.log("Small-molecule regulatory approval granted.");
  }
}

// Concrete implementation for Biologics
class BiologicsProcess {
  submit() {
    console.log("Submitting biologics clinical trial data...");
  }

  approve() {
    console.log("Biologics regulatory approval granted.");
  }
}

// Create instances and use the abstraction
const preclinicalSmallMolecule = new RegulatoryProcess(new SmallMoleculeDrugProcess());
preclinicalSmallMolecule.submit();
preclinicalSmallMolecule.approve();

const clinicalBiologics = new RegulatoryProcess(new SmallMoleculeDrugProcess());
clinicalBiologics.submit();
clinicalBiologics.approve();

const clinicalVaccine = new RegulatoryProcess(new VaccineProcess());
clinicalVaccine.submit();
clinicalVaccine.approve();

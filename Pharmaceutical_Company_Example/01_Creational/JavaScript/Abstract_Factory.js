// Abstract Factory Interface
class RegulatoryFactory {
  createSubmissionForm() {
    throw new Error("This method should be overridden by concrete factories!");
  }

  createTestingProtocol() {
    throw new Error("This method should be overridden by concrete factories!");
  }
}

// Concrete Factory for Vaccines
class VaccineRegulatoryFactory extends RegulatoryFactory {
  createSubmissionForm() {
    return new VaccineSubmissionForm();
  }

  createTestingProtocol() {
    return new VaccineTestingProtocol();
  }
}

// Concrete Factory for Small-Molecule Drugs
class SmallMoleculeRegulatoryFactory extends RegulatoryFactory {
  createSubmissionForm() {
    return new SmallMoleculeSubmissionForm();
  }

  createTestingProtocol() {
    return new SmallMoleculeTestingProtocol();
  }
}

// Concrete Factory for Biologics
class BiologicsRegulatoryFactory extends RegulatoryFactory {
  createSubmissionForm() {
    return new BiologicsSubmissionForm();
  }

  createTestingProtocol() {
    return new BiologicsTestingProtocol();
  }
}

// Abstract Product: Submission Form
class SubmissionForm {
  submit() {
    throw new Error("This method should be overridden by concrete products!");
  }
}

// Concrete Product: Vaccine Submission Form
class VaccineSubmissionForm extends SubmissionForm {
  submit() {
    console.log("Submitting vaccine clinical trial data form.");
  }
}

// Concrete Product: Small-Molecule Submission Form
class SmallMoleculeSubmissionForm extends SubmissionForm {
  submit() {
    console.log("Submitting small-molecule drug trial data form.");
  }
}

// Concrete Product: Biologics Submission Form
class BiologicsSubmissionForm extends SubmissionForm {
  submit() {
    console.log("Submitting biologics clinical trial data form.");
  }
}

// Abstract Product: Testing Protocol
class TestingProtocol {
  runTests() {
    throw new Error("This method should be overridden by concrete products!");
  }
}

// Concrete Product: Vaccine Testing Protocol
class VaccineTestingProtocol extends TestingProtocol {
  runTests() {
    console.log("Running tests for vaccines.");
  }
}

// Concrete Product: Small-Molecule Testing Protocol
class SmallMoleculeTestingProtocol extends TestingProtocol {
  runTests() {
    console.log("Running tests for small-molecule drugs.");
  }
}

// Concrete Product: Biologics Testing Protocol
class BiologicsTestingProtocol extends TestingProtocol {
  runTests() {
    console.log("Running tests for biologics.");
  }
}

// Function to process regulatory approval using the factory
function processRegulatoryApproval(factory) {
  const submissionForm = factory.createSubmissionForm();
  const testingProtocol = factory.createTestingProtocol();
  
  submissionForm.submit();
  testingProtocol.runTests();
}

// Vaccine Regulatory Process
const vaccineFactory = new VaccineRegulatoryFactory();
processRegulatoryApproval(vaccineFactory);

// Small-Molecule Drug Regulatory Process
const smallMoleculeFactory = new SmallMoleculeRegulatoryFactory();
processRegulatoryApproval(smallMoleculeFactory);

// Biologics Regulatory Process
const biologicsFactory = new BiologicsRegulatoryFactory();
processRegulatoryApproval(biologicsFactory);

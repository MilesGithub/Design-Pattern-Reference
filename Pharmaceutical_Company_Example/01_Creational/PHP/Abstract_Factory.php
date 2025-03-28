<?php

// Abstract Factory Interface
interface RegulatoryFactory {
    public function createSubmissionForm(): SubmissionForm;
    public function createTestingProtocol(): TestingProtocol;
}

// Concrete Factory for Vaccines
class VaccineRegulatoryFactory implements RegulatoryFactory {
    public function createSubmissionForm(): SubmissionForm {
        return new VaccineSubmissionForm();
    }

    public function createTestingProtocol(): TestingProtocol {
        return new VaccineTestingProtocol();
    }
}

// Concrete Factory for Small-Molecule Drugs
class SmallMoleculeRegulatoryFactory implements RegulatoryFactory {
    public function createSubmissionForm(): SubmissionForm {
        return new SmallMoleculeSubmissionForm();
    }

    public function createTestingProtocol(): TestingProtocol {
        return new SmallMoleculeTestingProtocol();
    }
}

// Concrete Factory for Biologics
class BiologicsRegulatoryFactory implements RegulatoryFactory {
    public function createSubmissionForm(): SubmissionForm {
        return new BiologicsSubmissionForm();
    }

    public function createTestingProtocol(): TestingProtocol {
        return new BiologicsTestingProtocol();
    }
}

// Abstract Product Interface for Submission Forms
interface SubmissionForm {
    public function submit(): void;
}

// Concrete Product: Vaccine Submission Form
class VaccineSubmissionForm implements SubmissionForm {
    public function submit(): void {
        echo "Submitting vaccine clinical trial data form.\n";
    }
}

// Concrete Product: Small-Molecule Submission Form
class SmallMoleculeSubmissionForm implements SubmissionForm {
    public function submit(): void {
        echo "Submitting small-molecule drug trial data form.\n";
    }
}

// Concrete Product: Biologics Submission Form
class BiologicsSubmissionForm implements SubmissionForm {
    public function submit(): void {
        echo "Submitting biologics clinical trial data form.\n";
    }
}

// Abstract Product Interface for Testing Protocols
interface TestingProtocol {
    public function runTests(): void;
}

// Concrete Product: Vaccine Testing Protocol
class VaccineTestingProtocol implements TestingProtocol {
    public function runTests(): void {
        echo "Running tests for vaccines.\n";
    }
}

// Concrete Product: Small-Molecule Testing Protocol
class SmallMoleculeTestingProtocol implements TestingProtocol {
    public function runTests(): void {
        echo "Running tests for small-molecule drugs.\n";
    }
}

// Concrete Product: Biologics Testing Protocol
class BiologicsTestingProtocol implements TestingProtocol {
    public function runTests(): void {
        echo "Running tests for biologics.\n";
    }
}

// Function to Process Regulatory Approval
function processRegulatoryApproval(RegulatoryFactory $factory): void {
    $submissionForm = $factory->createSubmissionForm();
    $testingProtocol = $factory->createTestingProtocol();
    
    $submissionForm->submit();
    $testingProtocol->runTests();
}

// Vaccine Regulatory Process
$vaccineFactory = new VaccineRegulatoryFactory();
processRegulatoryApproval($vaccineFactory);

// Small-Molecule Drug Regulatory Process
$smallMoleculeFactory = new SmallMoleculeRegulatoryFactory();
processRegulatoryApproval($smallMoleculeFactory);

// Biologics Regulatory Process
$biologicsFactory = new BiologicsRegulatoryFactory();
processRegulatoryApproval($biologicsFactory);

?>

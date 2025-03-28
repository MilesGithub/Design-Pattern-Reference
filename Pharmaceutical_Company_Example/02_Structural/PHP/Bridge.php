<?php

// Abstraction: RegulatoryProcess
class RegulatoryProcess {
    protected RegulatoryImplementation $implementation;

    public function __construct(RegulatoryImplementation $implementation) {
        $this->implementation = $implementation;
    }

    public function submit(): void {
        $this->implementation->submit();
    }

    public function approve(): void {
        $this->implementation->approve();
    }
}

// Implementation Interface
interface RegulatoryImplementation {
    public function submit(): void;
    public function approve(): void;
}

// Concrete Implementation for Vaccines
class VaccineProcess implements RegulatoryImplementation {
    public function submit(): void {
        echo "Submitting vaccine clinical trial data...\n";
    }

    public function approve(): void {
        echo "Vaccine regulatory approval granted.\n";
    }
}

// Concrete Implementation for Small-Molecule Drugs
class SmallMoleculeDrugProcess implements RegulatoryImplementation {
    public function submit(): void {
        echo "Submitting small-molecule clinical trial data...\n";
    }

    public function approve(): void {
        echo "Small-molecule regulatory approval granted.\n";
    }
}

// Concrete Implementation for Biologics
class BiologicsProcess implements RegulatoryImplementation {
    public function submit(): void {
        echo "Submitting biologics clinical trial data...\n";
    }

    public function approve(): void {
        echo "Biologics regulatory approval granted.\n";
    }
}

// Usage
$preclinicalSmallMolecule = new RegulatoryProcess(new SmallMoleculeDrugProcess());
$preclinicalSmallMolecule->submit();
$preclinicalSmallMolecule->approve();

$clinicalBiologics = new RegulatoryProcess(new BiologicsProcess());
$clinicalBiologics->submit();
$clinicalBiologics->approve();

$clinicalVaccine = new RegulatoryProcess(new VaccineProcess());
$clinicalVaccine->submit();
$clinicalVaccine->approve();

?>

<?php
// Product
class RegulatoryDocument {
    private $drug_name;
    private $clinical_trial_data;
    private $safety_report;
    private $manufacturing_data;

    public function __construct($drug_name) {
        $this->drug_name = $drug_name;
        $this->clinical_trial_data = null;
        $this->safety_report = null;
        $this->manufacturing_data = null;
    }

    public function showDocument() {
        echo "Regulatory Document for: {$this->drug_name}\n";
        echo "Clinical Trial Data: {$this->clinical_trial_data}\n";
        echo "Safety Report: {$this->safety_report}\n";
        echo "Manufacturing Data: {$this->manufacturing_data}\n";
    }

    public function setClinicalTrialData($data) {
        $this->clinical_trial_data = $data;
    }

    public function setSafetyReport($data) {
        $this->safety_report = $data;
    }

    public function setManufacturingData($data) {
        $this->manufacturing_data = $data;
    }
}

// Abstract Builder
abstract class RegulatoryDocumentBuilder {
    protected $document;

    public function __construct($drug_name) {
        $this->document = new RegulatoryDocument($drug_name);
    }

    abstract public function addClinicalTrialData();
    abstract public function addSafetyReport();
    abstract public function addManufacturingData();

    public function getDocument() {
        return $this->document;
    }
}

// Concrete Builder for Vaccines
class VaccineDocumentBuilder extends RegulatoryDocumentBuilder {
    public function addClinicalTrialData() {
        $this->document->setClinicalTrialData("Vaccine clinical trial data");
    }

    public function addSafetyReport() {
        $this->document->setSafetyReport("Vaccine safety report");
    }

    public function addManufacturingData() {
        $this->document->setManufacturingData("Vaccine manufacturing data");
    }
}

// Concrete Builder for Small-Molecule Drugs
class SmallMoleculeDocumentBuilder extends RegulatoryDocumentBuilder {
    public function addClinicalTrialData() {
        $this->document->setClinicalTrialData("Small-molecule clinical trial data");
    }

    public function addSafetyReport() {
        $this->document->setSafetyReport("Small-molecule safety report");
    }

    public function addManufacturingData() {
        $this->document->setManufacturingData("Small-molecule manufacturing data");
    }
}

// Concrete Builder for Biologics
class BiologicsDocumentBuilder extends RegulatoryDocumentBuilder {
    public function addClinicalTrialData() {
        $this->document->setClinicalTrialData("Biologics clinical trial data");
    }

    public function addSafetyReport() {
        $this->document->setSafetyReport("Biologics safety report");
    }

    public function addManufacturingData() {
        $this->document->setManufacturingData("Biologics manufacturing data");
    }
}

// Director: Manages the building process
class RegulatoryDirector {
    private $builder;

    public function __construct(RegulatoryDocumentBuilder $builder) {
        $this->builder = $builder;
    }

    public function constructDocument() {
        $this->builder->addClinicalTrialData();
        $this->builder->addSafetyReport();
        $this->builder->addManufacturingData();
    }

    public function getDocument() {
        return $this->builder->getDocument();
    }
}

// Create a director for a Vaccine regulatory document
$vaccineBuilder = new VaccineDocumentBuilder("Test Vaccine 01");
$director = new RegulatoryDirector($vaccineBuilder);
$director->constructDocument();
$vaccineDoc = $director->getDocument();
$vaccineDoc->showDocument();

// Create a director for a Small-Molecule regulatory document
$smallMoleculeBuilder = new SmallMoleculeDocumentBuilder("Test Small Molecule 01");
$director = new RegulatoryDirector($smallMoleculeBuilder);
$director->constructDocument();
$smallMoleculeDoc = $director->getDocument();
$smallMoleculeDoc->showDocument();

// Create a director for a Biologics regulatory document
$biologicsBuilder = new BiologicsDocumentBuilder("Test Monoclonal Antibody 01");
$director = new RegulatoryDirector($biologicsBuilder);
$director->constructDocument();
$biologicsDoc = $director->getDocument();
$biologicsDoc->showDocument();
?>
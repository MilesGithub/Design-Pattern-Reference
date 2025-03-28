<?php
// Product
class RegulatoryDocument {
    private $drug_name;
    private $document_type;

    public function __construct($drug_name, $document_type) {
        $this->drug_name = $drug_name;
        $this->document_type = $document_type;
    }

    public function showDocument() {
        echo "Regulatory Document for: {$this->drug_name}\n";
        echo "Type of Document: {$this->document_type}\n";
    }
}

// Abstract Creator
abstract class RegulatoryDocumentFactory {
    abstract public function createDocument($drug_name);
}

// Concrete Creator for Vaccine Documents
class VaccineDocumentFactory extends RegulatoryDocumentFactory {
    public function createDocument($drug_name) {
        return new RegulatoryDocument($drug_name, "Vaccine Regulatory Document");
    }
}

// Concrete Creator for Small-Molecule Documents
class SmallMoleculeDocumentFactory extends RegulatoryDocumentFactory {
    public function createDocument($drug_name) {
        return new RegulatoryDocument($drug_name, "Small-Molecule Regulatory Document");
    }
}

// Concrete Creator for Biologics Documents
class BiologicsDocumentFactory extends RegulatoryDocumentFactory {
    public function createDocument($drug_name) {
        return new RegulatoryDocument($drug_name, "Biologics Regulatory Document");
    }
}

// Function to process the document creation
function processDocument(RegulatoryDocumentFactory $factory, $drug_name) {
    $document = $factory->createDocument($drug_name);
    $document->showDocument();
}

// Example usage
$vaccineFactory = new VaccineDocumentFactory();
processDocument($vaccineFactory, "Test Vaccine 01");

$smallMoleculeFactory = new SmallMoleculeDocumentFactory();
processDocument($smallMoleculeFactory, "Test Small Molecule 01");

$biologicsFactory = new BiologicsDocumentFactory();
processDocument($biologicsFactory, "Test Monoclonal Antibody 01");

?>

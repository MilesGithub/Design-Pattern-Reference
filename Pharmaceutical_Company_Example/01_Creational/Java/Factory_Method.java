// Product
class RegulatoryDocument {
    private String drugName;
    private String documentType;

    public RegulatoryDocument(String drugName, String documentType) {
        this.drugName = drugName;
        this.documentType = documentType;
    }

    public void showDocument() {
        System.out.println("Regulatory Document for: " + drugName);
        System.out.println("Type of Document: " + documentType);
        System.out.println();
    }
}

// Abstract Creator (Factory)
abstract class RegulatoryDocumentFactory {
    public abstract RegulatoryDocument createDocument(String drugName);
}

// Concrete Creator for Vaccine Documents
class VaccineDocumentFactory extends RegulatoryDocumentFactory {
    public RegulatoryDocument createDocument(String drugName) {
        return new RegulatoryDocument(drugName, "Vaccine Regulatory Document");
    }
}

// Concrete Creator for Small-Molecule Documents
class SmallMoleculeDocumentFactory extends RegulatoryDocumentFactory {
    public RegulatoryDocument createDocument(String drugName) {
        return new RegulatoryDocument(drugName, "Small-Molecule Regulatory Document");
    }
}

// Concrete Creator for Biologics Documents
class BiologicsDocumentFactory extends RegulatoryDocumentFactory {
    public RegulatoryDocument createDocument(String drugName) {
        return new RegulatoryDocument(drugName, "Biologics Regulatory Document");
    }
}

// Client Code
public class Main {
    public static void processDocument(RegulatoryDocumentFactory factory, String drugName) {
        RegulatoryDocument document = factory.createDocument(drugName);
        document.showDocument();
    }

    public static void main(String[] args) {
        // Vaccine Regulatory Document
        RegulatoryDocumentFactory vaccineFactory = new VaccineDocumentFactory();
        processDocument(vaccineFactory, "Test Vaccine 01");

        // Small-Molecule Regulatory Document
        RegulatoryDocumentFactory smallMoleculeFactory = new SmallMoleculeDocumentFactory();
        processDocument(smallMoleculeFactory, "Test Small Molecule 01");

        // Biologics Regulatory Document
        RegulatoryDocumentFactory biologicsFactory = new BiologicsDocumentFactory();
        processDocument(biologicsFactory, "Test Monoclonal Antibody 01");
    }
}

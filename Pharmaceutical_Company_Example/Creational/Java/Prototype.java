// Prototype Interface
interface RegulatoryDocumentPrototype {
    RegulatoryDocumentPrototype cloneDocument(String newDrugName);
    void showDocument();
}

// Concrete Prototype
class RegulatoryDocument implements RegulatoryDocumentPrototype {
    private String drugName;
    private String documentType;
    private String clinicalTrialData;
    private String safetyReport;
    private String manufacturingData;

    public RegulatoryDocument(String drugName, String documentType, String clinicalTrialData, 
                              String safetyReport, String manufacturingData) {
        this.drugName = drugName;
        this.documentType = documentType;
        this.clinicalTrialData = clinicalTrialData;
        this.safetyReport = safetyReport;
        this.manufacturingData = manufacturingData;
    }

    // Cloning method
    @Override
    public RegulatoryDocumentPrototype cloneDocument(String newDrugName) {
        return new RegulatoryDocument(newDrugName, this.documentType, this.clinicalTrialData, 
                                      this.safetyReport, this.manufacturingData);
    }

    @Override
    public void showDocument() {
        System.out.println("Regulatory Document for: " + drugName);
        System.out.println("Document Type: " + documentType);
        System.out.println("Clinical Trial Data: " + clinicalTrialData);
        System.out.println("Safety Report: " + safetyReport);
        System.out.println("Manufacturing Data: " + manufacturingData);
        System.out.println();
    }
}

// Client Code
public class Main {
    public static void main(String[] args) {
        // Create prototypes
        RegulatoryDocument vaccinePrototype = new RegulatoryDocument(
            "Vaccine Prototype", "Vaccine Regulatory Document",
            "Standard vaccine clinical trial data",
            "Standard vaccine safety report",
            "Standard vaccine manufacturing data"
        );

        RegulatoryDocument smallMoleculePrototype = new RegulatoryDocument(
            "Small-Molecule Prototype", "Small-Molecule Regulatory Document",
            "Standard small-molecule clinical trial data",
            "Standard small-molecule safety report",
            "Standard small-molecule manufacturing data"
        );

        RegulatoryDocument biologicsPrototype = new RegulatoryDocument(
            "Biologics Prototype", "Biologics Regulatory Document",
            "Standard biologics clinical trial data",
            "Standard biologics safety report",
            "Standard biologics manufacturing data"
        );

        // Clone the vaccine prototype for a new vaccine
        RegulatoryDocument newVaccineDocument = (RegulatoryDocument) vaccinePrototype.cloneDocument("Test Vaccine 01");
        newVaccineDocument.showDocument();

        // Clone the small-molecule prototype for a new drug
        RegulatoryDocument newSmallMoleculeDocument = (RegulatoryDocument) smallMoleculePrototype.cloneDocument("Test Small Molecule 01");
        newSmallMoleculeDocument.showDocument();

        // Clone the biologics prototype for a new biologic drug
        RegulatoryDocument newBiologicsDocument = (RegulatoryDocument) biologicsPrototype.cloneDocument("Test Monoclonal Antibody 01");
        newBiologicsDocument.showDocument();
    }
}

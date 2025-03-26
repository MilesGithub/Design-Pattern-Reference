// Product
class RegulatoryDocument {
    private String drugName;
    private String clinicalTrialData;
    private String safetyReport;
    private String manufacturingData;

    public RegulatoryDocument(String drugName) {
        this.drugName = drugName;
    }

    public void setClinicalTrialData(String clinicalTrialData) {
        this.clinicalTrialData = clinicalTrialData;
    }

    public void setSafetyReport(String safetyReport) {
        this.safetyReport = safetyReport;
    }

    public void setManufacturingData(String manufacturingData) {
        this.manufacturingData = manufacturingData;
    }

    public void showDocument() {
        System.out.println("Regulatory Document for: " + drugName);
        System.out.println("Clinical Trial Data: " + clinicalTrialData);
        System.out.println("Safety Report: " + safetyReport);
        System.out.println("Manufacturing Data: " + manufacturingData);
        System.out.println();
    }
}

// Abstract Builder
abstract class RegulatoryDocumentBuilder {
    protected RegulatoryDocument document;

    public RegulatoryDocumentBuilder(String drugName) {
        this.document = new RegulatoryDocument(drugName);
    }

    public abstract void addClinicalTrialData();
    public abstract void addSafetyReport();
    public abstract void addManufacturingData();

    public RegulatoryDocument getDocument() {
        return document;
    }
}

// Concrete Builder for Vaccines
class VaccineDocumentBuilder extends RegulatoryDocumentBuilder {
    public VaccineDocumentBuilder(String drugName) {
        super(drugName);
    }

    public void addClinicalTrialData() {
        document.setClinicalTrialData("Vaccine clinical trial data");
    }

    public void addSafetyReport() {
        document.setSafetyReport("Vaccine safety report");
    }

    public void addManufacturingData() {
        document.setManufacturingData("Vaccine manufacturing data");
    }
}

// Concrete Builder for Small-Molecule Drugs
class SmallMoleculeDocumentBuilder extends RegulatoryDocumentBuilder {
    public SmallMoleculeDocumentBuilder(String drugName) {
        super(drugName);
    }

    public void addClinicalTrialData() {
        document.setClinicalTrialData("Small-molecule clinical trial data");
    }

    public void addSafetyReport() {
        document.setSafetyReport("Small-molecule safety report");
    }

    public void addManufacturingData() {
        document.setManufacturingData("Small-molecule manufacturing data");
    }
}

// Concrete Builder for Biologics
class BiologicsDocumentBuilder extends RegulatoryDocumentBuilder {
    public BiologicsDocumentBuilder(String drugName) {
        super(drugName);
    }

    public void addClinicalTrialData() {
        document.setClinicalTrialData("Biologics clinical trial data");
    }

    public void addSafetyReport() {
        document.setSafetyReport("Biologics safety report");
    }

    public void addManufacturingData() {
        document.setManufacturingData("Biologics manufacturing data");
    }
}

// Director: Manages the building process
class RegulatoryDirector {
    private RegulatoryDocumentBuilder builder;

    public RegulatoryDirector(RegulatoryDocumentBuilder builder) {
        this.builder = builder;
    }

    public void constructDocument() {
        builder.addClinicalTrialData();
        builder.addSafetyReport();
        builder.addManufacturingData();
    }

    public RegulatoryDocument getDocument() {
        return builder.getDocument();
    }
}

// Client Code
public class Main {
    public static void main(String[] args) {
        // Vaccine Regulatory Document
        RegulatoryDocumentBuilder vaccineBuilder = new VaccineDocumentBuilder("Test Vaccine 01");
        RegulatoryDirector director = new RegulatoryDirector(vaccineBuilder);
        director.constructDocument();
        RegulatoryDocument vaccineDoc = director.getDocument();
        vaccineDoc.showDocument();

        // Small-Molecule Regulatory Document
        RegulatoryDocumentBuilder smallMoleculeBuilder = new SmallMoleculeDocumentBuilder("Test Small Molecule 01");
        director = new RegulatoryDirector(smallMoleculeBuilder);
        director.constructDocument();
        RegulatoryDocument smallMoleculeDoc = director.getDocument();
        smallMoleculeDoc.showDocument();

        // Biologics Regulatory Document
        RegulatoryDocumentBuilder biologicsBuilder = new BiologicsDocumentBuilder("Test Monoclonal Antibody 01");
        director = new RegulatoryDirector(biologicsBuilder);
        director.constructDocument();
        RegulatoryDocument biologicsDoc = director.getDocument();
        biologicsDoc.showDocument();
    }
}

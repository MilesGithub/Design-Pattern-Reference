// Interface for the implementation
interface RegulatoryImplementation {
    void submit();
    void approve();
}

// Abstraction class
class RegulatoryProcess {
    private RegulatoryImplementation implementation;

    public RegulatoryProcess(RegulatoryImplementation implementation) {
        this.implementation = implementation;
    }

    public void submit() {
        implementation.submit();
    }

    public void approve() {
        implementation.approve();
    }
}

// Concrete implementation for Vaccines
class VaccineProcess implements RegulatoryImplementation {
    public void submit() {
        System.out.println("Submitting vaccine clinical trial data...");
    }

    public void approve() {
        System.out.println("Vaccine regulatory approval granted.");
    }
}

// Concrete implementation for Small-Molecule Drugs
class SmallMoleculeDrugProcess implements RegulatoryImplementation {
    public void submit() {
        System.out.println("Submitting small-molecule clinical trial data...");
    }

    public void approve() {
        System.out.println("Small-molecule regulatory approval granted.");
    }
}

// Concrete implementation for Biologics
class BiologicsProcess implements RegulatoryImplementation {
    public void submit() {
        System.out.println("Submitting biologics clinical trial data...");
    }

    public void approve() {
        System.out.println("Biologics regulatory approval granted.");
    }
}

// Main class to demonstrate usage
public class Main {
    public static void main(String[] args) {
        RegulatoryProcess preclinicalSmallMolecule = new RegulatoryProcess(new SmallMoleculeDrugProcess());
        preclinicalSmallMolecule.submit();
        preclinicalSmallMolecule.approve();

        RegulatoryProcess clinicalBiologics = new RegulatoryProcess(new BiologicsProcess());
        clinicalBiologics.submit();
        clinicalBiologics.approve();

        RegulatoryProcess clinicalVaccine = new RegulatoryProcess(new VaccineProcess());
        clinicalVaccine.submit();
        clinicalVaccine.approve();
    }
}

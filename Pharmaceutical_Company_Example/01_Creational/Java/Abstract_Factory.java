// Abstract Factory Interface
interface RegulatoryFactory {
    SubmissionForm createSubmissionForm();
    TestingProtocol createTestingProtocol();
}

// Concrete Factory for Vaccines
class VaccineRegulatoryFactory implements RegulatoryFactory {
    public SubmissionForm createSubmissionForm() {
        return new VaccineSubmissionForm();
    }

    public TestingProtocol createTestingProtocol() {
        return new VaccineTestingProtocol();
    }
}

// Concrete Factory for Small-Molecule Drugs
class SmallMoleculeRegulatoryFactory implements RegulatoryFactory {
    public SubmissionForm createSubmissionForm() {
        return new SmallMoleculeSubmissionForm();
    }

    public TestingProtocol createTestingProtocol() {
        return new SmallMoleculeTestingProtocol();
    }
}

// Concrete Factory for Biologics
class BiologicsRegulatoryFactory implements RegulatoryFactory {
    public SubmissionForm createSubmissionForm() {
        return new BiologicsSubmissionForm();
    }

    public TestingProtocol createTestingProtocol() {
        return new BiologicsTestingProtocol();
    }
}

// Abstract Product: Submission Form
interface SubmissionForm {
    void submit();
}

// Concrete Product: Vaccine Submission Form
class VaccineSubmissionForm implements SubmissionForm {
    public void submit() {
        System.out.println("Submitting vaccine clinical trial data form.");
    }
}

// Concrete Product: Small-Molecule Submission Form
class SmallMoleculeSubmissionForm implements SubmissionForm {
    public void submit() {
        System.out.println("Submitting small-molecule drug trial data form.");
    }
}

// Concrete Product: Biologics Submission Form
class BiologicsSubmissionForm implements SubmissionForm {
    public void submit() {
        System.out.println("Submitting biologics clinical trial data form.");
    }
}

// Abstract Product: Testing Protocol
interface TestingProtocol {
    void runTests();
}

// Concrete Product: Vaccine Testing Protocol
class VaccineTestingProtocol implements TestingProtocol {
    public void runTests() {
        System.out.println("Running tests for vaccines.");
    }
}

// Concrete Product: Small-Molecule Testing Protocol
class SmallMoleculeTestingProtocol implements TestingProtocol {
    public void runTests() {
        System.out.println("Running tests for small-molecule drugs.");
    }
}

// Concrete Product: Biologics Testing Protocol
class BiologicsTestingProtocol implements TestingProtocol {
    public void runTests() {
        System.out.println("Running tests for biologics.");
    }
}

// Client Code to process regulatory approval
public class Main {
    public static void processRegulatoryApproval(RegulatoryFactory factory) {
        SubmissionForm submissionForm = factory.createSubmissionForm();
        TestingProtocol testingProtocol = factory.createTestingProtocol();

        submissionForm.submit();
        testingProtocol.runTests();
    }

    public static void main(String[] args) {
        // Vaccine Regulatory Process
        RegulatoryFactory vaccineFactory = new VaccineRegulatoryFactory();
        processRegulatoryApproval(vaccineFactory);

        System.out.println();

        // Small-Molecule Drug Regulatory Process
        RegulatoryFactory smallMoleculeFactory = new SmallMoleculeRegulatoryFactory();
        processRegulatoryApproval(smallMoleculeFactory);

        System.out.println();

        // Biologics Regulatory Process
        RegulatoryFactory biologicsFactory = new BiologicsRegulatoryFactory();
        processRegulatoryApproval(biologicsFactory);
    }
}

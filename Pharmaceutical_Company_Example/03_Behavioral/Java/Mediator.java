// Mediator Interface
interface Mediator {
    void notify(String sender, String event);
}

// Concrete Mediator
class RegulatoryMediator implements Mediator {
    private ClinicalTrials clinicalTrials;
    private QualityAssurance qualityAssurance;
    private RegulatoryAffairs regulatoryAffairs;
    private LegalDepartment legal;

    public void setClinicalTrials(ClinicalTrials clinicalTrials) {
        this.clinicalTrials = clinicalTrials;
    }

    public void setQualityAssurance(QualityAssurance qualityAssurance) {
        this.qualityAssurance = qualityAssurance;
    }

    public void setRegulatoryAffairs(RegulatoryAffairs regulatoryAffairs) {
        this.regulatoryAffairs = regulatoryAffairs;
    }

    public void setLegal(LegalDepartment legal) {
        this.legal = legal;
    }

    @Override
    public void notify(String sender, String event) {
        switch (event) {
            case "Clinical Trial Completed":
                System.out.println("Mediator: Clinical Trial completed. Notifying Quality Assurance.");
                if (qualityAssurance != null) {
                    qualityAssurance.checkQuality();
                }
                break;
            case "Quality Check Completed":
                System.out.println("Mediator: Quality Check completed. Notifying Regulatory Affairs.");
                if (regulatoryAffairs != null) {
                    regulatoryAffairs.prepareDocuments();
                }
                break;
            case "Documents Prepared":
                System.out.println("Mediator: Documents prepared. Notifying Legal Department.");
                if (legal != null) {
                    legal.reviewDocuments();
                }
                break;
            case "Legal Review Completed":
                System.out.println("Mediator: Legal Review completed. Drug is ready for final approval.");
                break;
            default:
                break;
        }
    }
}

// Department Interface
abstract class Department {
    protected Mediator mediator;

    public Department(Mediator mediator) {
        this.mediator = mediator;
    }

    public abstract void completeTask();
}

// Concrete Department: Clinical Trials
class ClinicalTrials extends Department {
    public ClinicalTrials(Mediator mediator) {
        super(mediator);
    }

    public void runTrials() {
        System.out.println("Clinical Trials: Running clinical trials...");
        mediator.notify("ClinicalTrials", "Clinical Trial Completed");
    }

    @Override
    public void completeTask() {
        runTrials();
    }
}

// Concrete Department: Quality Assurance
class QualityAssurance extends Department {
    public QualityAssurance(Mediator mediator) {
        super(mediator);
    }

    public void checkQuality() {
        System.out.println("Quality Assurance: Checking product quality...");
        mediator.notify("QualityAssurance", "Quality Check Completed");
    }

    @Override
    public void completeTask() {
        checkQuality();
    }
}

// Concrete Department: Regulatory Affairs
class RegulatoryAffairs extends Department {
    public RegulatoryAffairs(Mediator mediator) {
        super(mediator);
    }

    public void prepareDocuments() {
        System.out.println("Regulatory Affairs: Preparing regulatory documents...");
        mediator.notify("RegulatoryAffairs", "Documents Prepared");
    }

    @Override
    public void completeTask() {
        prepareDocuments();
    }
}

// Concrete Department: Legal Department
class LegalDepartment extends Department {
    public LegalDepartment(Mediator mediator) {
        super(mediator);
    }

    public void reviewDocuments() {
        System.out.println("Legal Department: Reviewing regulatory documents...");
        mediator.notify("LegalDepartment", "Legal Review Completed");
    }

    @Override
    public void completeTask() {
        reviewDocuments();
    }
}

public class Main {
    public static void main(String[] args) {
        // Create Mediator
        RegulatoryMediator mediator = new RegulatoryMediator();

        // Create Departments
        ClinicalTrials clinicalTrials = new ClinicalTrials(mediator);
        QualityAssurance qualityAssurance = new QualityAssurance(mediator);
        RegulatoryAffairs regulatoryAffairs = new RegulatoryAffairs(mediator);
        LegalDepartment legal = new LegalDepartment(mediator);

        // Set Departments in the Mediator
        mediator.setClinicalTrials(clinicalTrials);
        mediator.setQualityAssurance(qualityAssurance);
        mediator.setRegulatoryAffairs(regulatoryAffairs);
        mediator.setLegal(legal);

        // Run process
        clinicalTrials.runTrials();
    }
}

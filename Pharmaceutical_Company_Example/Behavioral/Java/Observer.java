import java.util.ArrayList;
import java.util.List;

// Observer Interface
interface Observer {
    void update(String state);
}

// Subject
class DrugApprovalProcess {
    private List<Observer> observers = new ArrayList<>();
    private String state;

    public void attachObserver(Observer observer) {
        observers.add(observer);
    }

    public void detachObserver(Observer observer) {
        observers.remove(observer);
    }

    public void notifyObservers() {
        System.out.println("DrugApprovalProcess: Notifying observers about state change to: " + state);
        for (Observer observer : observers) {
            observer.update(state);
        }
    }

    public void setState(String newState) {
        this.state = newState;
        System.out.println("DrugApprovalProcess: State changed to: " + state);
        notifyObservers();
    }
}

// Concrete Observer: Clinical Trials Department
class ClinicalTrials implements Observer {
    @Override
    public void update(String state) {
        System.out.println("Clinical Trials Department: Notified about state change to: " + state);
    }
}

// Concrete Observer: Quality Assurance Department
class QualityAssurance implements Observer {
    @Override
    public void update(String state) {
        System.out.println("Quality Assurance Department: Notified about state change to: " + state);
    }
}

// Concrete Observer: Legal Department
class LegalDepartment implements Observer {
    @Override
    public void update(String state) {
        System.out.println("Legal Department: Notified about state change to: " + state);
    }
}

// Concrete Observer: Regulatory Affairs Department
class RegulatoryAffairs implements Observer {
    @Override
    public void update(String state) {
        System.out.println("Regulatory Affairs Department: Notified about state change to: " + state);
    }
}

public class Main {
    public static void main(String[] args) {
        // Create the DrugApprovalProcess (Subject)
        DrugApprovalProcess drugApprovalProcess = new DrugApprovalProcess();

        // Create observers
        ClinicalTrials clinicalTrials = new ClinicalTrials();
        QualityAssurance qualityAssurance = new QualityAssurance();
        LegalDepartment legal = new LegalDepartment();
        RegulatoryAffairs regulatoryAffairs = new RegulatoryAffairs();

        // Attach observers to the subject
        drugApprovalProcess.attachObserver(clinicalTrials);
        drugApprovalProcess.attachObserver(qualityAssurance);
        drugApprovalProcess.attachObserver(legal);
        drugApprovalProcess.attachObserver(regulatoryAffairs);

        // Simulate state changes and notify observers
        drugApprovalProcess.setState("Clinical Trial Started");
        drugApprovalProcess.setState("Clinical Trial Completed");
        drugApprovalProcess.setState("Quality Check in Progress");
        drugApprovalProcess.setState("Under Regulatory Review");
        drugApprovalProcess.setState("Approved");
    }
}

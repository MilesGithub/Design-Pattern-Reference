// Abstract class for the drug approval process
abstract class DrugApprovalProcess {
    public abstract void applyForApproval(String drugName);
}

// Real implementation of the drug approval process
class RealDrugApprovalProcess extends DrugApprovalProcess {
    @Override
    public void applyForApproval(String drugName) {
        System.out.println("Processing approval for drug: " + drugName);
    }
}

// Proxy class that controls access to the RealDrugApprovalProcess
class DrugApprovalProxy extends DrugApprovalProcess {
    private RealDrugApprovalProcess realSubject;

    public DrugApprovalProxy() {
        this.realSubject = new RealDrugApprovalProcess();
    }

    // Method to check authorization
    private boolean checkAuthorization() {
        System.out.println("Checking authorization...");
        return true; // Or false for unauthorized access
    }

    @Override
    public void applyForApproval(String drugName) {
        if (checkAuthorization()) {
            realSubject.applyForApproval(drugName);
        } else {
            System.out.println("Unauthorized access");
        }
    }
}

// Helper function to request approval
public class DrugApprovalRequest {
    public static void requestApproval(DrugApprovalProxy proxy, String drugType) {
        System.out.println("\nRequesting approval for " + drugType + "...");
        proxy.applyForApproval(drugType);
    }

    public static void main(String[] args) {
        // Create a Proxy instance
        DrugApprovalProxy proxy = new DrugApprovalProxy();

        // Request approval for different drug types
        requestApproval(proxy, "Test Vaccine 01");
        requestApproval(proxy, "Test Small Molecule 01");
        requestApproval(proxy, "Test Biologics 01");
    }
}

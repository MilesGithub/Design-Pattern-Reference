import java.util.HashMap;
import java.util.Map;

public class RegulatoryApprovalSystem {
    // Static variable to hold the one instance
    private static RegulatoryApprovalSystem instance;

    // Internal storage for approvals
    private Map<String, String> approvals;

    // Private constructor to prevent external instantiation
    private RegulatoryApprovalSystem() {
        approvals = new HashMap<>();
    }

    // Public static method to get the single instance
    public static synchronized RegulatoryApprovalSystem getInstance() {
        if (instance == null) {
            instance = new RegulatoryApprovalSystem();
        }
        return instance;
    }

    // Add approval
    public void addApproval(String drugName, String status) {
        approvals.put(drugName, status);
        System.out.println("Added approval status for: " + drugName + " - Status: " + status);
    }

    // Get status
    public void getStatus(String drugName) {
        if (approvals.containsKey(drugName)) {
            System.out.println("Approval status for " + drugName + " is: " + approvals.get(drugName));
        } else {
            System.out.println("No approval status found for " + drugName);
        }
    }

    // Show all approvals
    public void showAllApprovals() {
        System.out.println("Current approval statuses:");
        for (Map.Entry<String, String> entry : approvals.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
    }

    // Main method for demonstration
    public static void main(String[] args) {
        RegulatoryApprovalSystem approvalSystem = RegulatoryApprovalSystem.getInstance();

        // Add approvals
        approvalSystem.addApproval("Test Vaccine 01", "Approved");
        approvalSystem.addApproval("Test Small Molecule 01", "Under Review");
        approvalSystem.addApproval("Test Monoclonal Antibody 01", "Approved");

        // Check status
        approvalSystem.getStatus("Test Small Molecule 01");
        approvalSystem.getStatus("Test Vaccine 01");

        // Show all approvals
        approvalSystem.showAllApprovals();

        // Create another instance
        RegulatoryApprovalSystem approvalSystem2 = RegulatoryApprovalSystem.getInstance();
        approvalSystem2.addApproval("Test Small Molecule 02", "Pending Review");

        // Verify shared instance
        approvalSystem2.showAllApprovals();
        approvalSystem.showAllApprovals();
    }
}

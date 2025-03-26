// Strategy Interface
interface RegulatoryStrategy {
    void approveApplication(String drugName);
}

// Concrete Strategy: Standard Approval
class StandardApprovalStrategy implements RegulatoryStrategy {
    @Override
    public void approveApplication(String drugName) {
        System.out.println("Applying Standard Approval Process for drug: " + drugName);
        System.out.println(drugName + " has been approved using the Standard Approval Strategy.");
    }
}

// Concrete Strategy: Accelerated Approval
class AcceleratedApprovalStrategy implements RegulatoryStrategy {
    @Override
    public void approveApplication(String drugName) {
        System.out.println("Applying Accelerated Approval Process for drug: " + drugName);
        System.out.println(drugName + " has been approved using the Accelerated Approval Strategy.");
    }
}

// Context
class DrugApprovalContext {
    private RegulatoryStrategy strategy;

    public DrugApprovalContext(RegulatoryStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(RegulatoryStrategy newStrategy) {
        this.strategy = newStrategy;
    }

    public void approveDrug(String drugName) {
        strategy.approveApplication(drugName);
    }
}

// Main class to test the Strategy pattern
public class Main {
    public static void main(String[] args) {
        // Create Context with Standard Approval Strategy
        DrugApprovalContext approvalContext = new DrugApprovalContext(new StandardApprovalStrategy());

        // Approve drug using Standard Approval Strategy
        approvalContext.approveDrug("Test Small Molecule 01");

        // Switch to Accelerated Approval Strategy
        approvalContext.setStrategy(new AcceleratedApprovalStrategy());
        approvalContext.approveDrug("Test Small Molecule 02");
    }
}

// Define Abstract Class with Template Method
abstract class RegulatoryProcess {
    public final void executeProcess(String drugName) {
        System.out.println("Starting the regulatory process for drug: " + drugName);
        performEvaluation(drugName);
        performApproval(drugName);
        finalizeProcess(drugName);
        System.out.println("Regulatory process completed for drug: " + drugName);
    }

    // Abstract Methods (to be implemented by subclasses)
    protected abstract void performEvaluation(String drugName);
    protected abstract void performApproval(String drugName);

    // Concrete Method (can be overridden but has default behavior)
    protected void finalizeProcess(String drugName) {
        System.out.println("Finalizing process for drug: " + drugName);
    }
}

// Concrete Class: Standard Approval Process
class StandardApprovalProcess extends RegulatoryProcess {
    @Override
    protected void performEvaluation(String drugName) {
        System.out.println("Evaluating drug: " + drugName + " using Standard Evaluation.");
    }

    @Override
    protected void performApproval(String drugName) {
        System.out.println("Approving drug: " + drugName + " using Standard Approval Process.");
    }
}

// Concrete Class: Accelerated Approval Process
class AcceleratedApprovalProcess extends RegulatoryProcess {
    @Override
    protected void performEvaluation(String drugName) {
        System.out.println("Evaluating drug: " + drugName + " using Accelerated Evaluation.");
    }

    @Override
    protected void performApproval(String drugName) {
        System.out.println("Approving drug: " + drugName + " using Accelerated Approval Process.");
    }
}

// Main class to test the Template Method pattern
public class Main {
    public static void main(String[] args) {
        // Create instances of the concrete classes
        RegulatoryProcess standardProcess = new StandardApprovalProcess();
        RegulatoryProcess acceleratedProcess = new AcceleratedApprovalProcess();

        // Execute processes
        standardProcess.executeProcess("Test Small Molecule 01");
        System.out.println();
        acceleratedProcess.executeProcess("Test Small Molecule 02");
    }
}

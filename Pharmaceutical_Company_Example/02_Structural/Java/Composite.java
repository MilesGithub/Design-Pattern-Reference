// Component: Abstract class for Regulatory Process
abstract class RegulatoryProcess {
    public abstract void execute();
}

// Leaf: Represents individual steps in the regulatory process
class Step extends RegulatoryProcess {
    private String stepName;

    public Step(String stepName) {
        this.stepName = stepName;
    }

    @Override
    public void execute() {
        System.out.println("Executing step: " + stepName);
    }
}

// Composite: Represents composite processes made up of steps or other processes
class CompositeProcess extends RegulatoryProcess {
    private String processName;
    private List<RegulatoryProcess> children = new ArrayList<>();

    public CompositeProcess(String processName) {
        this.processName = processName;
    }

    public void add(RegulatoryProcess process) {
        children.add(process);
    }

    public void remove(RegulatoryProcess process) {
        children.remove(process);
    }

    @Override
    public void execute() {
        System.out.println("Executing composite process: " + processName);
        for (RegulatoryProcess child : children) {
            child.execute();
        }
    }
}

// Client code
public class Main {
    public static void main(String[] args) {
        // Leaf objects - individual steps
        RegulatoryProcess clinicalTrialStep = new Step("Clinical Trial Approval");
        RegulatoryProcess safetyStep = new Step("Safety Review");
        RegulatoryProcess manufacturingStep = new Step("Manufacturing Validation");

        // Composite processes
        CompositeProcess clinicalProcess = new CompositeProcess("Clinical Process");
        clinicalProcess.add(clinicalTrialStep);

        CompositeProcess regulatoryProcess = new CompositeProcess("Regulatory Process");
        regulatoryProcess.add(safetyStep);
        regulatoryProcess.add(manufacturingStep);

        CompositeProcess fullApprovalProcess = new CompositeProcess("Full Drug Approval Process");
        fullApprovalProcess.add(clinicalProcess);
        fullApprovalProcess.add(regulatoryProcess);

        // Execute the full approval process
        fullApprovalProcess.execute();
    }
}

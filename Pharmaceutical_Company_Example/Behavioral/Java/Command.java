// Command Interface
interface RegulatoryCommand {
    void execute();
}

// Concrete Command: Submit Drug Application
class SubmitApplicationCommand implements RegulatoryCommand {
    private String drugName;
    private RegulatorySystem system;

    public SubmitApplicationCommand(String drugName, RegulatorySystem system) {
        this.drugName = drugName;
        this.system = system;
    }

    @Override
    public void execute() {
        system.submitApplication(drugName);
    }
}

// Concrete Command: Approve Drug
class ApproveDrugCommand implements RegulatoryCommand {
    private String drugName;
    private RegulatorySystem system;

    public ApproveDrugCommand(String drugName, RegulatorySystem system) {
        this.drugName = drugName;
        this.system = system;
    }

    @Override
    public void execute() {
        system.approveDrug(drugName);
    }
}

// Concrete Command: Reject Drug
class RejectDrugCommand implements RegulatoryCommand {
    private String drugName;
    private RegulatorySystem system;

    public RejectDrugCommand(String drugName, RegulatorySystem system) {
        this.drugName = drugName;
        this.system = system;
    }

    @Override
    public void execute() {
        system.rejectDrug(drugName);
    }
}

// Receiver
class RegulatorySystem {
    private java.util.Map<String, Boolean> applications;
    private java.util.Map<String, String> status;

    public RegulatorySystem() {
        applications = new java.util.HashMap<>();
        status = new java.util.HashMap<>();
    }

    public void submitApplication(String drugName) {
        applications.put(drugName, true);
        status.put(drugName, "Submitted");
        System.out.println("Application submitted for: " + drugName);
    }

    public void approveDrug(String drugName) {
        if (applications.containsKey(drugName)) {
            status.put(drugName, "Approved");
            System.out.println(drugName + " approved.");
        } else {
            System.out.println("No application found for: " + drugName);
        }
    }

    public void rejectDrug(String drugName) {
        if (applications.containsKey(drugName)) {
            status.put(drugName, "Rejected");
            System.out.println(drugName + " rejected.");
        } else {
            System.out.println("No application found for: " + drugName);
        }
    }

    public void showStatus(String drugName) {
        if (status.containsKey(drugName)) {
            System.out.println("Current status of " + drugName + ": " + status.get(drugName));
        } else {
            System.out.println("No status found for: " + drugName);
        }
    }
}

// Invoker
class ApprovalSystemInvoker {
    private java.util.List<RegulatoryCommand> commands;

    public ApprovalSystemInvoker() {
        commands = new java.util.ArrayList<>();
    }

    public void addCommand(RegulatoryCommand command) {
        commands.add(command);
    }

    public void executeCommands() {
        for (RegulatoryCommand command : commands) {
            command.execute();
        }
        commands.clear(); // Clear the command queue after execution
    }
}

public class Main {
    public static void main(String[] args) {
        // Create Receiver
        RegulatorySystem regulatorySystem = new RegulatorySystem();

        // Create Invoker
        ApprovalSystemInvoker approvalSystemInvoker = new ApprovalSystemInvoker();

        // Add commands to invoker
        SubmitApplicationCommand submitVaccineCommand = new SubmitApplicationCommand("Test Small Molecule 01", regulatorySystem);
        ApproveDrugCommand approveVaccineCommand = new ApproveDrugCommand("Test Small Molecule 01", regulatorySystem);
        RejectDrugCommand rejectAspirinCommand = new RejectDrugCommand("Test Small Molecule 02", regulatorySystem);

        approvalSystemInvoker.addCommand(submitVaccineCommand);
        approvalSystemInvoker.addCommand(approveVaccineCommand);
        approvalSystemInvoker.addCommand(rejectAspirinCommand);

        // Execute all commands
        approvalSystemInvoker.executeCommands();

        // Show the status of drugs after executing commands
        regulatorySystem.showStatus("Test Small Molecule 01");
        regulatorySystem.showStatus("Test Small Molecule 02");
    }
}

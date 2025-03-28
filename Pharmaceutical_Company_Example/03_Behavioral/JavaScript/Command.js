// Command Interface
class RegulatoryCommand {
    execute() {
        throw new Error("This method should be overridden!");
    }
}

// Concrete Command: Submit Drug Application
class SubmitApplicationCommand extends RegulatoryCommand {
    constructor(drugName, system) {
        super();
        this.drugName = drugName;
        this.system = system;
    }

    execute() {
        this.system.submitApplication(this.drugName);
    }
}

// Concrete Command: Approve Drug
class ApproveDrugCommand extends RegulatoryCommand {
    constructor(drugName, system) {
        super();
        this.drugName = drugName;
        this.system = system;
    }

    execute() {
        this.system.approveDrug(this.drugName);
    }
}

// Concrete Command: Reject Drug
class RejectDrugCommand extends RegulatoryCommand {
    constructor(drugName, system) {
        super();
        this.drugName = drugName;
        this.system = system;
    }

    execute() {
        this.system.rejectDrug(this.drugName);
    }
}

// Receiver
class RegulatorySystem {
    constructor() {
        this.applications = {};
        this.status = {};
    }

    submitApplication(drugName) {
        this.applications[drugName] = true;
        this.status[drugName] = "Submitted";
        console.log(`Application submitted for: ${drugName}`);
    }

    approveDrug(drugName) {
        if (this.applications[drugName]) {
            this.status[drugName] = "Approved";
            console.log(`${drugName} approved.`);
        } else {
            console.log(`No application found for: ${drugName}`);
        }
    }

    rejectDrug(drugName) {
        if (this.applications[drugName]) {
            this.status[drugName] = "Rejected";
            console.log(`${drugName} rejected.`);
        } else {
            console.log(`No application found for: ${drugName}`);
        }
    }

    showStatus(drugName) {
        if (this.status[drugName]) {
            console.log(`Current status of ${drugName}: ${this.status[drugName]}`);
        } else {
            console.log(`No status found for: ${drugName}`);
        }
    }
}

// Invoker
class ApprovalSystemInvoker {
    constructor() {
        this.commands = [];
    }

    addCommand(command) {
        this.commands.push(command);
    }

    executeCommands() {
        this.commands.forEach(command => command.execute());
        this.commands = []; // Clear the queue after execution
    }
}

// Create Receiver
const regulatorySystem = new RegulatorySystem();

// Create Invoker
const approvalSystemInvoker = new ApprovalSystemInvoker();

// Add commands to invoker
const submitVaccineCommand = new SubmitApplicationCommand("Test Small Molecule 01", regulatorySystem);
const approveVaccineCommand = new ApproveDrugCommand("Test Small Molecule 01", regulatorySystem);
const rejectAspirinCommand = new RejectDrugCommand("Test Small Molecule 02", regulatorySystem);

approvalSystemInvoker.addCommand(submitVaccineCommand);
approvalSystemInvoker.addCommand(approveVaccineCommand);
approvalSystemInvoker.addCommand(rejectAspirinCommand);

// Execute commands
approvalSystemInvoker.executeCommands();

// Show status of drugs after executing commands
regulatorySystem.showStatus("Test Small Molecule 01");
regulatorySystem.showStatus("Test Small Molecule 02");

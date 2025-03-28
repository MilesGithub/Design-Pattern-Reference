// Component (Abstract class)
class RegulatoryProcess {
    execute() {
        throw new Error("This method should be implemented by subclasses.");
    }
}

// Leaf class - Step
class Step extends RegulatoryProcess {
    constructor(stepName) {
        super();
        this.stepName = stepName;
    }

    execute() {
        console.log(`Executing step: ${this.stepName}`);
    }
}

// Composite class - CompositeProcess
class CompositeProcess extends RegulatoryProcess {
    constructor(processName) {
        super();
        this.processName = processName;
        this.children = [];
    }

    add(regulatoryProcess) {
        this.children.push(regulatoryProcess);
    }

    remove(regulatoryProcess) {
        const index = this.children.indexOf(regulatoryProcess);
        if (index > -1) {
            this.children.splice(index, 1);
        }
    }

    execute() {
        console.log(`Executing composite process: ${this.processName}`);
        for (let child of this.children) {
            child.execute();
        }
    }
}

// Leaf objects - individual steps
const clinicalTrialStep = new Step("Clinical Trial Approval");
const safetyStep = new Step("Safety Review");
const manufacturingStep = new Step("Manufacturing Validation");

// Composite processes
const clinicalProcess = new CompositeProcess("Clinical Process");
clinicalProcess.add(clinicalTrialStep);

const regulatoryProcess = new CompositeProcess("Regulatory Process");
regulatoryProcess.add(safetyStep);
regulatoryProcess.add(manufacturingStep);

const fullApprovalProcess = new CompositeProcess("Full Drug Approval Process");
fullApprovalProcess.add(clinicalProcess);
fullApprovalProcess.add(regulatoryProcess);

// Execute the full approval process
fullApprovalProcess.execute();

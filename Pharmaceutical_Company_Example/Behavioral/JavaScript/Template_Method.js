// Define Abstract Class with Template Method
class RegulatoryProcess {
  executeProcess(drugName) {
    console.log(`Starting the regulatory process for drug: ${drugName}`);
    this.performEvaluation(drugName);
    this.performApproval(drugName);
    this.finalizeProcess(drugName);
    console.log(`Regulatory process completed for drug: ${drugName}`);
  }

  // Abstract Methods (To be implemented by subclasses)
  performEvaluation(drugName) {
    throw new Error("This method should be overridden by concrete classes!");
  }

  performApproval(drugName) {
    throw new Error("This method should be overridden by concrete classes!");
  }

  finalizeProcess(drugName) {
    console.log(`Finalizing process for drug: ${drugName}`);
  }
}

// Concrete Class: Standard Approval Process
class StandardApprovalProcess extends RegulatoryProcess {
  performEvaluation(drugName) {
    console.log(`Evaluating drug: ${drugName} using Standard Evaluation.`);
  }

  performApproval(drugName) {
    console.log(`Approving drug: ${drugName} using Standard Approval Process.`);
  }
}

// Concrete Class: Accelerated Approval Process
class AcceleratedApprovalProcess extends RegulatoryProcess {
  performEvaluation(drugName) {
    console.log(`Evaluating drug: ${drugName} using Accelerated Evaluation.`);
  }

  performApproval(drugName) {
    console.log(`Approving drug: ${drugName} using Accelerated Approval Process.`);
  }
}

// Create instances of the concrete classes
const standardProcess = new StandardApprovalProcess();
const acceleratedProcess = new AcceleratedApprovalProcess();

// Execute processes
standardProcess.executeProcess("Test Small Molecule 01");
acceleratedProcess.executeProcess("Test Small Molecule 02");

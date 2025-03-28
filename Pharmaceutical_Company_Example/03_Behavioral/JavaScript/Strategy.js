// Define the Strategy Interface
class RegulatoryStrategy {
  approveApplication(drugName) {
    throw new Error("This method should be overridden by concrete strategies!");
  }
}

// Concrete Strategy: Standard Approval
class StandardApprovalStrategy extends RegulatoryStrategy {
  approveApplication(drugName) {
    console.log(`Applying Standard Approval Process for drug: ${drugName}`);
    console.log(`${drugName} has been approved using the Standard Approval Strategy.`);
  }
}

// Concrete Strategy: Accelerated Approval
class AcceleratedApprovalStrategy extends RegulatoryStrategy {
  approveApplication(drugName) {
    console.log(`Applying Accelerated Approval Process for drug: ${drugName}`);
    console.log(`${drugName} has been approved using the Accelerated Approval Strategy.`);
  }
}

// Context
class DrugApprovalContext {
  constructor(strategy) {
    this._strategy = strategy;
  }

  setStrategy(newStrategy) {
    this._strategy = newStrategy;
  }

  approveDrug(drugName) {
    this._strategy.approveApplication(drugName);
  }
}

// Example Usage
// Create Context
const approvalContext = new DrugApprovalContext(new StandardApprovalStrategy());

// Set Standard Approval Strategy
approvalContext.approveDrug("Test Small Molecule 01");

// Set Accelerated Approval Strategy
approvalContext.setStrategy(new AcceleratedApprovalStrategy());
approvalContext.approveDrug("Test Small Molecule 02");

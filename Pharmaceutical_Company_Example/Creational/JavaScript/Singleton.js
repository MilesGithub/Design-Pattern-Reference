class RegulatoryApprovalSystem {
  constructor() {
    if (RegulatoryApprovalSystem._instance) {
      return RegulatoryApprovalSystem._instance;
    }

    this.approvals = {};
    RegulatoryApprovalSystem._instance = this;
  }

  // Add approval status for a drug
  addApproval(drugName, status) {
    this.approvals[drugName] = status;
    console.log(`Added approval status for: ${drugName} - Status: ${status}`);
  }

  // Get approval status for a drug
  getStatus(drugName) {
    if (this.approvals[drugName]) {
      console.log(`Approval status for ${drugName} is: ${this.approvals[drugName]}`);
    } else {
      console.log(`No approval status found for ${drugName}`);
    }
  }

  // Show all approval statuses
  showAllApprovals() {
    console.log("Current approval statuses:");
    for (let drug in this.approvals) {
      console.log(`${drug} : ${this.approvals[drug]}`);
    }
  }
}

// Get the single instance of RegulatoryApprovalSystem
const approvalSystem = new RegulatoryApprovalSystem();

// Add approvals
approvalSystem.addApproval("Test Vaccine 01", "Approved");
approvalSystem.addApproval("Test Small Molecule 01", "Under Review");
approvalSystem.addApproval("Test Monoclonal Antibody 01", "Approved");

approvalSystem.getStatus("Test Small Molecule 01");
approvalSystem.getStatus("Test Vaccine 01");

approvalSystem.showAllApprovals();

// Create another instance (it will return the same instance)
const approvalSystem2 = new RegulatoryApprovalSystem();
approvalSystem2.addApproval("Test Small Molecule 02", "Pending Review");

// Two instances are the same
approvalSystem2.showAllApprovals();
approvalSystem.showAllApprovals();

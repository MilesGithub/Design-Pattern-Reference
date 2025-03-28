// Subject (Abstract Class)
class DrugApprovalProcess {
    applyForApproval(drugName) {
        throw new Error("This method should be overridden in subclasses.");
    }
}

// Real Subject
class RealDrugApprovalProcess extends DrugApprovalProcess {
    applyForApproval(drugName) {
        console.log(`Processing approval for drug: ${drugName}`);
    }
}

// Proxy Class
class DrugApprovalProxy extends DrugApprovalProcess {
    constructor() {
        super();
        this.realSubject = new RealDrugApprovalProcess();
    }

    checkAuthorization() {
        console.log("Checking authorization...");
        return true; // Change to false to simulate unauthorized access
    }

    applyForApproval(drugName) {
        if (this.checkAuthorization()) {
            this.realSubject.applyForApproval(drugName);
        } else {
            console.log("Unauthorized access");
        }
    }
}

// Function to request approval through the proxy
function requestApproval(proxy, drugType) {
    console.log(`\nRequesting approval for ${drugType}...`);
    proxy.applyForApproval(drugType);
}

// Create a Proxy instance
const proxy = new DrugApprovalProxy();

// Request approval for different drug types
requestApproval(proxy, "Test Vaccine 01");
requestApproval(proxy, "Test Small Molecule 01");
requestApproval(proxy, "Test Biologics 01");

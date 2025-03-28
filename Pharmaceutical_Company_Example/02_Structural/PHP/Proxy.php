<?php

// Abstract class
abstract class DrugApprovalProcess {
    abstract public function applyForApproval(string $drugName): void;
}

// Real subject
class RealDrugApprovalProcess extends DrugApprovalProcess {
    public function applyForApproval(string $drugName): void {
        echo "Processing approval for drug: {$drugName}\n";
    }
}

// Proxy class
class DrugApprovalProxy extends DrugApprovalProcess {
    private RealDrugApprovalProcess $realSubject;

    public function __construct() {
        $this->realSubject = new RealDrugApprovalProcess();
    }

    private function checkAuthorization(): bool {
        echo "Checking authorization...\n";
        return true;  // Return false for unauthorized access
    }

    public function applyForApproval(string $drugName): void {
        if ($this->checkAuthorization()) {
            $this->realSubject->applyForApproval($drugName);
        } else {
            echo "Unauthorized access\n";
        }
    }
}

// Function to request approval
function requestApproval(DrugApprovalProxy $proxy, string $drugType): void {
    echo "\nRequesting approval for {$drugType}...\n";
    $proxy->applyForApproval($drugType);
}

// Create a Proxy instance
$proxy = new DrugApprovalProxy();

// Request approval for different drug types
requestApproval($proxy, "Test Vaccine 01");
requestApproval($proxy, "Test Small Molecule 01");
requestApproval($proxy, "Test Biologics 01");

?>

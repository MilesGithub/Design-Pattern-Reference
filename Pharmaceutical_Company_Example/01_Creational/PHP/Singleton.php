<?php

// Singleton
class RegulatoryApprovalSystem {
    private static $instance = null;
    private $approvals = [];

    private function __construct() {
        // Private constructor to prevent direct instantiation
    }

    // Method to get the single instance of the class
    public static function getInstance() {
        if (self::$instance === null) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    // Add an approval status
    public function addApproval($drugName, $status) {
        $this->approvals[$drugName] = $status;
        echo "Added approval status for: $drugName - Status: $status\n";
    }

    // Get the approval status
    public function getStatus($drugName) {
        if (array_key_exists($drugName, $this->approvals)) {
            echo "Approval status for $drugName is: {$this->approvals[$drugName]}\n";
        } else {
            echo "No approval status found for $drugName\n";
        }
    }

    // Show all approvals
    public function showAllApprovals() {
        echo "Current approval statuses:\n";
        foreach ($this->approvals as $drug => $status) {
            echo "$drug : $status\n";
        }
    }
}

// Get the single instance of RegulatoryApprovalSystem
$approvalSystem = RegulatoryApprovalSystem::getInstance();

// Add approvals
$approvalSystem->addApproval("Test Vaccine 01", "Approved");
$approvalSystem->addApproval("Test Small Molecule 01", "Under Review");
$approvalSystem->addApproval("Test Monoclonal Antibody 01", "Approved");

$approvalSystem->getStatus("Test Small Molecule 01");
$approvalSystem->getStatus("Test Vaccine 01");

$approvalSystem->showAllApprovals();

// Create another instance (it will return the same instance)
$approvalSystem2 = RegulatoryApprovalSystem::getInstance();
$approvalSystem2->addApproval("Test Small Molecule 02", "Pending Review");

// Two instances are the same
$approvalSystem2->showAllApprovals();
$approvalSystem->showAllApprovals();

?>

<?php

// Define the Strategy Interface
interface RegulatoryStrategy
{
    public function approveApplication(string $drugName): void;
}

// Concrete Strategy: Standard Approval
class StandardApprovalStrategy implements RegulatoryStrategy
{
    public function approveApplication(string $drugName): void
    {
        echo "Applying Standard Approval Process for drug: $drugName\n";
        echo "$drugName has been approved using the Standard Approval Strategy.\n";
    }
}

// Concrete Strategy: Accelerated Approval
class AcceleratedApprovalStrategy implements RegulatoryStrategy
{
    public function approveApplication(string $drugName): void
    {
        echo "Applying Accelerated Approval Process for drug: $drugName\n";
        echo "$drugName has been approved using the Accelerated Approval Strategy.\n";
    }
}

// Context
class DrugApprovalContext
{
    private RegulatoryStrategy $strategy;

    public function __construct(RegulatoryStrategy $strategy)
    {
        $this->strategy = $strategy;
    }

    public function setStrategy(RegulatoryStrategy $newStrategy): void
    {
        $this->strategy = $newStrategy;
    }

    public function approveDrug(string $drugName): void
    {
        $this->strategy->approveApplication($drugName);
    }
}

// Example Usage
// Create Context
$approvalContext = new DrugApprovalContext(new StandardApprovalStrategy());

// Set Standard Approval Strategy
$approvalContext->approveDrug("Test Small Molecule 01");

// Set Accelerated Approval Strategy
$approvalContext->setStrategy(new AcceleratedApprovalStrategy());
$approvalContext->approveDrug("Test Small Molecule 02");

?>

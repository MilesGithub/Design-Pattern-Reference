<?php

// Abstract Class with Template Method
abstract class RegulatoryProcess
{
    public function executeProcess(string $drugName): void
    {
        echo "Starting the regulatory process for drug: $drugName\n";
        $this->performEvaluation($drugName);
        $this->performApproval($drugName);
        $this->finalizeProcess($drugName);
        echo "Regulatory process completed for drug: $drugName\n";
    }

    // Abstract Methods
    abstract protected function performEvaluation(string $drugName): void;
    abstract protected function performApproval(string $drugName): void;

    // Final Method
    protected function finalizeProcess(string $drugName): void
    {
        echo "Finalizing process for drug: $drugName\n";
    }
}

// Concrete Class: Standard Approval Process
class StandardApprovalProcess extends RegulatoryProcess
{
    protected function performEvaluation(string $drugName): void
    {
        echo "Evaluating drug: $drugName using Standard Evaluation.\n";
    }

    protected function performApproval(string $drugName): void
    {
        echo "Approving drug: $drugName using Standard Approval Process.\n";
    }
}

// Concrete Class: Accelerated Approval Process
class AcceleratedApprovalProcess extends RegulatoryProcess
{
    protected function performEvaluation(string $drugName): void
    {
        echo "Evaluating drug: $drugName using Accelerated Evaluation.\n";
    }

    protected function performApproval(string $drugName): void
    {
        echo "Approving drug: $drugName using Accelerated Approval Process.\n";
    }
}

// Create instances of the concrete classes
$standardProcess = new StandardApprovalProcess();
$acceleratedProcess = new AcceleratedApprovalProcess();

// Execute processes
$standardProcess->executeProcess("Test Small Molecule 01");
$acceleratedProcess->executeProcess("Test Small Molecule 02");

?>

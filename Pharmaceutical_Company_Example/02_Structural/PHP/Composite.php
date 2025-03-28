<?php

// Component: RegulatoryProcess
abstract class RegulatoryProcess {
    abstract public function execute(): void;
}

// Leaf: Step (Individual Steps in the Process)
class Step extends RegulatoryProcess {
    private string $stepName;

    public function __construct(string $stepName) {
        $this->stepName = $stepName;
    }

    public function execute(): void {
        echo "Executing step: {$this->stepName}\n";
    }
}

// Composite: CompositeProcess (A Collection of Steps)
class CompositeProcess extends RegulatoryProcess {
    private string $processName;
    private array $children = [];

    public function __construct(string $processName) {
        $this->processName = $processName;
    }

    public function add(RegulatoryProcess $regulatoryProcess): void {
        $this->children[] = $regulatoryProcess;
    }

    public function remove(RegulatoryProcess $regulatoryProcess): void {
        $index = array_search($regulatoryProcess, $this->children, true);
        if ($index !== false) {
            array_splice($this->children, $index, 1);
        }
    }

    public function execute(): void {
        echo "Executing composite process: {$this->processName}\n";
        foreach ($this->children as $child) {
            $child->execute();
        }
    }
}

// Leaf objects - individual steps
$clinicalTrialStep = new Step("Clinical Trial Approval");
$safetyStep = new Step("Safety Review");
$manufacturingStep = new Step("Manufacturing Validation");

// Composite processes
$clinicalProcess = new CompositeProcess("Clinical Process");
$clinicalProcess->add($clinicalTrialStep);

$regulatoryProcess = new CompositeProcess("Regulatory Process");
$regulatoryProcess->add($safetyStep);
$regulatoryProcess->add($manufacturingStep);

$fullApprovalProcess = new CompositeProcess("Full Drug Approval Process");
$fullApprovalProcess->add($clinicalProcess);
$fullApprovalProcess->add($regulatoryProcess);

$fullApprovalProcess->execute();

?>

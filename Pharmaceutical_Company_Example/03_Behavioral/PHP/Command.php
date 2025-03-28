<?php

// Command Interface
abstract class RegulatoryCommand {
    abstract public function execute();
}

// Concrete Command: Submit Drug Application
class SubmitApplicationCommand extends RegulatoryCommand {
    private $drug_name;
    private $system;

    public function __construct($drug_name, $system) {
        $this->drug_name = $drug_name;
        $this->system = $system;
    }

    public function execute() {
        $this->system->submitApplication($this->drug_name);
    }
}

// Concrete Command: Approve Drug
class ApproveDrugCommand extends RegulatoryCommand {
    private $drug_name;
    private $system;

    public function __construct($drug_name, $system) {
        $this->drug_name = $drug_name;
        $this->system = $system;
    }

    public function execute() {
        $this->system->approveDrug($this->drug_name);
    }
}

// Concrete Command: Reject Drug
class RejectDrugCommand extends RegulatoryCommand {
    private $drug_name;
    private $system;

    public function __construct($drug_name, $system) {
        $this->drug_name = $drug_name;
        $this->system = $system;
    }

    public function execute() {
        $this->system->rejectDrug($this->drug_name);
    }
}

// Receiver
class RegulatorySystem {
    private $applications = [];
    private $status = [];

    public function submitApplication($drug_name) {
        $this->applications[$drug_name] = true;
        $this->status[$drug_name] = "Submitted";
        echo "Application submitted for: " . $drug_name . "\n";
    }

    public function approveDrug($drug_name) {
        if (isset($this->applications[$drug_name])) {
            $this->status[$drug_name] = "Approved";
            echo $drug_name . " approved.\n";
        } else {
            echo "No application found for: " . $drug_name . "\n";
        }
    }

    public function rejectDrug($drug_name) {
        if (isset($this->applications[$drug_name])) {
            $this->status[$drug_name] = "Rejected";
            echo $drug_name . " rejected.\n";
        } else {
            echo "No application found for: " . $drug_name . "\n";
        }
    }

    public function showStatus($drug_name) {
        if (isset($this->status[$drug_name])) {
            echo "Current status of " . $drug_name . ": " . $this->status[$drug_name] . "\n";
        } else {
            echo "No status found for: " . $drug_name . "\n";
        }
    }
}

// Invoker
class ApprovalSystemInvoker {
    private $commands = [];

    public function addCommand($command) {
        $this->commands[] = $command;
    }

    public function executeCommands() {
        foreach ($this->commands as $command) {
            $command->execute();
        }
        $this->commands = [];  // Clear the command queue after execution
    }
}

// Create Receiver
$regulatorySystem = new RegulatorySystem();

// Create Invoker
$approvalSystemInvoker = new ApprovalSystemInvoker();

// Add commands to invoker
$submitVaccineCommand = new SubmitApplicationCommand("Test Small Molecule 01", $regulatorySystem);
$approveVaccineCommand = new ApproveDrugCommand("Test Small Molecule 01", $regulatorySystem);
$rejectAspirinCommand = new RejectDrugCommand("Test Small Molecule 02", $regulatorySystem);

$approvalSystemInvoker->addCommand($submitVaccineCommand);
$approvalSystemInvoker->addCommand($approveVaccineCommand);
$approvalSystemInvoker->addCommand($rejectAspirinCommand);

$approvalSystemInvoker->executeCommands();

// Show the status of drugs after executing commands
$regulatorySystem->showStatus("Test Small Molecule 01");
$regulatorySystem->showStatus("Test Small Molecule 02");

?>

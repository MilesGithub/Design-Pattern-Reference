<?php

// Base class for a drug approval request handler
abstract class DrugApprovalHandler {
    protected ?DrugApprovalHandler $nextHandler = null;

    public function setNext(DrugApprovalHandler $handler): DrugApprovalHandler {
        $this->nextHandler = $handler;
        return $handler;
    }

    abstract public function handleRequest(array $drug): void;

    protected function passToNext(array $drug): void {
        if ($this->nextHandler) {
            $this->nextHandler->handleRequest($drug);
        } else {
            echo "End of chain, no handler could process the request.\n";
        }
    }
}

// Concrete handler for Initial Review
class InitialReviewHandler extends DrugApprovalHandler {
    public function handleRequest(array $drug): void {
        if ($drug['initial_review_status'] == "Pending") {
            echo "Initial review passed for {$drug['name']}\n";
            $drug['initial_review_status'] = "Approved";
            $this->passToNext($drug);
        } else {
            echo "Initial review already processed for {$drug['name']}\n";
            $this->passToNext($drug);
        }
    }
}

// Concrete handler for Clinical Trials Review
class ClinicalTrialsHandler extends DrugApprovalHandler {
    public function handleRequest(array $drug): void {
        if ($drug['clinical_trials_status'] == "Pending") {
            echo "Clinical trials review passed for {$drug['name']}\n";
            $drug['clinical_trials_status'] = "Approved";
            $this->passToNext($drug);
        } else {
            echo "Clinical trials already processed for {$drug['name']}\n";
            $this->passToNext($drug);
        }
    }
}

// Concrete handler for Regulatory Review
class RegulatoryReviewHandler extends DrugApprovalHandler {
    public function handleRequest(array $drug): void {
        if ($drug['regulatory_status'] == "Pending") {
            echo "Regulatory review passed for {$drug['name']}\n";
            $drug['regulatory_status'] = "Approved";
            $this->passToNext($drug);
        } else {
            echo "Regulatory review already processed for {$drug['name']}\n";
            $this->passToNext($drug);
        }
    }
}

// Concrete handler for Final Approval
class FinalApprovalHandler extends DrugApprovalHandler {
    public function handleRequest(array $drug): void {
        if ($drug['initial_review_status'] == "Approved" &&
            $drug['clinical_trials_status'] == "Approved" &&
            $drug['regulatory_status'] == "Approved") {
            echo "Final approval granted for {$drug['name']}\n";
            $drug['final_approval_status'] = "Approved";
        } else {
            echo "Drug {$drug['name']} could not pass final approval.\n";
        }
    }
}

$drug1 = [
    'name' => "Test Small Molecule 01",
    'initial_review_status' => "Pending",
    'clinical_trials_status' => "Pending",
    'regulatory_status' => "Pending",
    'final_approval_status' => "Pending"
];

// Setup the chain of responsibility
$initialReview = new InitialReviewHandler();
$clinicalTrials = new ClinicalTrialsHandler();
$regulatoryReview = new RegulatoryReviewHandler();
$finalApproval = new FinalApprovalHandler();

$initialReview->setNext($clinicalTrials)
              ->setNext($regulatoryReview)
              ->setNext($finalApproval);

$initialReview->handleRequest($drug1);

?>

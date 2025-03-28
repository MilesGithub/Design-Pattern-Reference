<?php

// Observer Interface
interface Observer
{
    public function update(string $state): void;
}

// Subject
class DrugApprovalProcess
{
    private array $observers = [];
    private string $state = "";

    public function attachObserver(Observer $observer): void
    {
        $this->observers[] = $observer;
    }

    public function detachObserver(Observer $observer): void
    {
        $this->observers = array_filter($this->observers, fn($obs) => $obs !== $observer);
    }

    public function notifyObservers(): void
    {
        echo "DrugApprovalProcess: Notifying observers about state change to: {$this->state}\n";
        foreach ($this->observers as $observer) {
            $observer->update($this->state);
        }
    }

    public function setState(string $newState): void
    {
        $this->state = $newState;
        echo "DrugApprovalProcess: State changed to: {$this->state}\n";
        $this->notifyObservers();
    }
}

// Concrete Observer: Clinical Trials Department
class ClinicalTrials implements Observer
{
    public function update(string $state): void
    {
        echo "Clinical Trials Department: Notified about state change to: {$state}\n";
    }
}

// Concrete Observer: Quality Assurance Department
class QualityAssurance implements Observer
{
    public function update(string $state): void
    {
        echo "Quality Assurance Department: Notified about state change to: {$state}\n";
    }
}

// Concrete Observer: Legal Department
class LegalDepartment implements Observer
{
    public function update(string $state): void
    {
        echo "Legal Department: Notified about state change to: {$state}\n";
    }
}

// Concrete Observer: Regulatory Affairs Department
class RegulatoryAffairs implements Observer
{
    public function update(string $state): void
    {
        echo "Regulatory Affairs Department: Notified about state change to: {$state}\n";
    }
}

// Create the DrugApprovalProcess (Subject)
$drugApprovalProcess = new DrugApprovalProcess();

// Create observers
$clinicalTrials = new ClinicalTrials();
$qualityAssurance = new QualityAssurance();
$legal = new LegalDepartment();
$regulatoryAffairs = new RegulatoryAffairs();

// Attach observers to the subject
$drugApprovalProcess->attachObserver($clinicalTrials);
$drugApprovalProcess->attachObserver($qualityAssurance);
$drugApprovalProcess->attachObserver($legal);
$drugApprovalProcess->attachObserver($regulatoryAffairs);

// Simulate state changes and notify observers
$drugApprovalProcess->setState("Clinical Trial Started");
$drugApprovalProcess->setState("Clinical Trial Completed");
$drugApprovalProcess->setState("Quality Check in Progress");
$drugApprovalProcess->setState("Under Regulatory Review");
$drugApprovalProcess->setState("Approved");

?>

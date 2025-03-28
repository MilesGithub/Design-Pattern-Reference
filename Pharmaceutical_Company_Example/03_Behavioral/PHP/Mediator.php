<?php

// Mediator Interface
interface Mediator
{
    public function notify(string $sender, string $event): void;
}

// Concrete Mediator
class RegulatoryMediator implements Mediator
{
    private ?ClinicalTrials $clinicalTrials = null;
    private ?QualityAssurance $qualityAssurance = null;
    private ?RegulatoryAffairs $regulatoryAffairs = null;
    private ?LegalDepartment $legal = null;

    public function notify(string $sender, string $event): void
    {
        switch ($event) {
            case "Clinical Trial Completed":
                echo "Mediator: Clinical Trial completed. Notifying Quality Assurance.\n";
                if ($this->qualityAssurance) {
                    $this->qualityAssurance->checkQuality();
                }
                break;

            case "Quality Check Completed":
                echo "Mediator: Quality Check completed. Notifying Regulatory Affairs.\n";
                if ($this->regulatoryAffairs) {
                    $this->regulatoryAffairs->prepareDocuments();
                }
                break;

            case "Documents Prepared":
                echo "Mediator: Documents prepared. Notifying Legal Department.\n";
                if ($this->legal) {
                    $this->legal->reviewDocuments();
                }
                break;

            case "Legal Review Completed":
                echo "Mediator: Legal Review completed. Drug is ready for final approval.\n";
                break;
        }
    }

    // Setters for departments
    public function setClinicalTrials(ClinicalTrials $clinicalTrials): void
    {
        $this->clinicalTrials = $clinicalTrials;
    }

    public function setQualityAssurance(QualityAssurance $qualityAssurance): void
    {
        $this->qualityAssurance = $qualityAssurance;
    }

    public function setRegulatoryAffairs(RegulatoryAffairs $regulatoryAffairs): void
    {
        $this->regulatoryAffairs = $regulatoryAffairs;
    }

    public function setLegal(LegalDepartment $legal): void
    {
        $this->legal = $legal;
    }
}

// Department Interfaces
abstract class Department
{
    protected Mediator $mediator;

    public function __construct(Mediator $mediator)
    {
        $this->mediator = $mediator;
    }

    abstract public function completeTask(): void;
}

// Concrete Department: Clinical Trials
class ClinicalTrials extends Department
{
    public function runTrials(): void
    {
        echo "Clinical Trials: Running clinical trials...\n";
        $this->mediator->notify("ClinicalTrials", "Clinical Trial Completed");
    }

    public function completeTask(): void
    {
        // Task completion logic
    }
}

// Concrete Department: Quality Assurance
class QualityAssurance extends Department
{
    public function checkQuality(): void
    {
        echo "Quality Assurance: Checking product quality...\n";
        $this->mediator->notify("QualityAssurance", "Quality Check Completed");
    }

    public function completeTask(): void
    {
        // Task completion logic
    }
}

// Concrete Department: Regulatory Affairs
class RegulatoryAffairs extends Department
{
    public function prepareDocuments(): void
    {
        echo "Regulatory Affairs: Preparing regulatory documents...\n";
        $this->mediator->notify("RegulatoryAffairs", "Documents Prepared");
    }

    public function completeTask(): void
    {
        // Task completion logic
    }
}

// Concrete Department: Legal Department
class LegalDepartment extends Department
{
    public function reviewDocuments(): void
    {
        echo "Legal Department: Reviewing regulatory documents...\n";
        $this->mediator->notify("LegalDepartment", "Legal Review Completed");
    }

    public function completeTask(): void
    {
        // Task completion logic
    }
}

// Create the Mediator
$mediator = new RegulatoryMediator();

// Create Departments
$clinicalTrials = new ClinicalTrials($mediator);
$qualityAssurance = new QualityAssurance($mediator);
$regulatoryAffairs = new RegulatoryAffairs($mediator);
$legal = new LegalDepartment($mediator);

// Set Departments in the Mediator
$mediator->setClinicalTrials($clinicalTrials);
$mediator->setQualityAssurance($qualityAssurance);
$mediator->setRegulatoryAffairs($regulatoryAffairs);
$mediator->setLegal($legal);

// Run process
$clinicalTrials->runTrials();

?>

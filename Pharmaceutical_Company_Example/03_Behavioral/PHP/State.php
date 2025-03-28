<?php

// State interface
interface DrugState
{
    public function proceedToNext(DrugApplication $drugApplication): void;
    public function getStateName(): string;
}

// Submitted State
class SubmittedState implements DrugState
{
    public function proceedToNext(DrugApplication $drugApplication): void
    {
        echo "Proceeding from Submitted to Clinical Trial...\n";
        $drugApplication->setState(new ClinicalTrialState());
    }

    public function getStateName(): string
    {
        return "Submitted";
    }
}

// Clinical Trial State
class ClinicalTrialState implements DrugState
{
    public function proceedToNext(DrugApplication $drugApplication): void
    {
        echo "Proceeding from Clinical Trial to Under Review...\n";
        $drugApplication->setState(new UnderReviewState());
    }

    public function getStateName(): string
    {
        return "Clinical Trial";
    }
}

// Under Review State
class UnderReviewState implements DrugState
{
    public function proceedToNext(DrugApplication $drugApplication): void
    {
        echo "Proceeding from Under Review to Approved...\n";
        $drugApplication->setState(new ApprovedState());
    }

    public function getStateName(): string
    {
        return "Under Review";
    }
}

// Approved State
class ApprovedState implements DrugState
{
    public function proceedToNext(DrugApplication $drugApplication): void
    {
        echo "The drug has already been approved. No further states.\n";
    }

    public function getStateName(): string
    {
        return "Approved";
    }
}

// Context class
class DrugApplication
{
    private DrugState $state;

    public function __construct(DrugState $state)
    {
        $this->state = $state;
    }

    public function setState(DrugState $newState): void
    {
        $this->state = $newState;
        echo "DrugApplication: State changed to: " . $this->state->getStateName() . "\n";
    }

    public function proceed(): void
    {
        $this->state->proceedToNext($this);
    }

    public function getCurrentState(): string
    {
        return $this->state->getStateName();
    }
}

// Initial drug application in "Submitted" state
$drugApplication = new DrugApplication(new SubmittedState());

$drugApplication->proceed();  // Moves to Clinical Trial
$drugApplication->proceed();  // Moves to Under Review
$drugApplication->proceed();  // Moves to Approved
$drugApplication->proceed();  // Already Approved, no further state

?>

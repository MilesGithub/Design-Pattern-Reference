<?php

// Memento
class DrugApplicationMemento
{
    private string $state;

    public function __construct(string $state)
    {
        $this->state = $state;
    }

    public function getState(): string
    {
        return $this->state;
    }
}

// Originator
class DrugApplication
{
    private string $state;

    public function __construct()
    {
        $this->state = "";
    }

    public function setState(string $newState): void
    {
        $this->state = $newState;
        echo "DrugApplication: State has changed to: {$this->state}\n";
    }

    public function createMemento(): DrugApplicationMemento
    {
        return new DrugApplicationMemento($this->state);
    }

    public function restoreMemento(DrugApplicationMemento $memento): void
    {
        $this->state = $memento->getState();
        echo "DrugApplication: State restored to: {$this->state}\n";
    }
}

// Caretaker
class ApplicationCaretaker
{
    private array $mementos = [];

    public function saveMemento(DrugApplicationMemento $memento): void
    {
        $this->mementos[] = $memento;
        echo "ApplicationCaretaker: Saved state.\n";
    }

    public function getMemento(int $index): DrugApplicationMemento
    {
        if ($index >= 0 && $index < count($this->mementos)) {
            return $this->mementos[$index];
        } else {
            throw new Exception("Invalid index for memento retrieval.");
        }
    }
}

// Create the DrugApplication and ApplicationCaretaker instances
$drugApplication = new DrugApplication();
$caretaker = new ApplicationCaretaker();

// Set initial state
$drugApplication->setState("Submitted");
$caretaker->saveMemento($drugApplication->createMemento());

// Change state to clinical trial and save
$drugApplication->setState("Clinical Trial");
$caretaker->saveMemento($drugApplication->createMemento());

// Change state to review and save
$drugApplication->setState("Under Review");
$caretaker->saveMemento($drugApplication->createMemento());

// Change state to approved
$drugApplication->setState("Approved");

// Restore to previous state: Under Review
$drugApplication->restoreMemento($caretaker->getMemento(2));

// Restore to an earlier state: Clinical Trial
$drugApplication->restoreMemento($caretaker->getMemento(1));

// Restore to the initial state: Submitted
$drugApplication->restoreMemento($caretaker->getMemento(0));

?>

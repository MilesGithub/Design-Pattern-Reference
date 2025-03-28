<?php

// Flyweight class
class RegulatoryProcessFlyweight {
    private array $commonRegulatorySteps;

    public function __construct() {
        $this->commonRegulatorySteps = [
            "Submit Trial Data",
            "Review Trial Data",
            "Submit Safety Data",
            "Review Safety Data",
            "Submit Regulatory Documents",
            "Obtain Regulatory Approval"
        ];
    }

    public function getSteps(): array {
        return $this->commonRegulatorySteps;
    }
}

// Flyweight Factory
class FlyweightFactory {
    private array $flyweights = [];

    public function getFlyweight(string $key): RegulatoryProcessFlyweight {
        if (!isset($this->flyweights[$key])) {
            echo "Creating new flyweight for: {$key}\n";
            $this->flyweights[$key] = new RegulatoryProcessFlyweight();
        } else {
            echo "Reusing existing flyweight for: {$key}\n";
        }
        return $this->flyweights[$key];
    }
}

// Uses flyweights for shared regulatory processes
class Drug {
    private string $name;
    private RegulatoryProcessFlyweight $flyweight;
    private array $regulatorySteps;

    public function __construct(string $name, RegulatoryProcessFlyweight $flyweight) {
        $this->name = $name;
        $this->flyweight = $flyweight;
        $this->regulatorySteps = $flyweight->getSteps();
    }

    public function displayRegulatoryProcess(): void {
        echo "Regulatory process for {$this->name}:\n";
        foreach ($this->regulatorySteps as $step) {
            echo " - {$step}\n";
        }
    }
}

// Create Flyweight Factory
$flyweightFactory = new FlyweightFactory();

// Create Drugs and use Flyweight instances
$drug1 = new Drug("Test Small Molecule 01", $flyweightFactory->getFlyweight("Standard Process"));
$drug2 = new Drug("Test Small Molecule 02", $flyweightFactory->getFlyweight("Standard Process"));
$drug3 = new Drug("Test Monoclonal Antibody 01", $flyweightFactory->getFlyweight("Standard Process"));

// Display regulatory processes
$drug1->displayRegulatoryProcess();
$drug2->displayRegulatoryProcess();
$drug3->displayRegulatoryProcess();

?>

<?php

// Adaptee: ClinicalTrialSystem
class ClinicalTrialSystem {
    private string $trialData;

    public function __construct(string $drugName) {
        $this->trialData = "{$drugName} clinical trial data";
    }

    public function getTrialData(): string {
        return $this->trialData;
    }
}

// Target: RegulatoryAPI
class RegulatoryAPI {
    public function uploadDataToRegulator(string $data): void {
        echo "Uploading the following data to regulatory authorities: $data\n";
    }
}

// Adapter: Bridges ClinicalTrialSystem (Adaptee) and RegulatoryAPI (Target)
class RegulatoryAdapter {
    private ClinicalTrialSystem $clinicalTrialSystem;
    private RegulatoryAPI $regulatoryAPI;

    public function __construct(ClinicalTrialSystem $clinicalTrialSystem, RegulatoryAPI $regulatoryAPI) {
        $this->clinicalTrialSystem = $clinicalTrialSystem;
        $this->regulatoryAPI = $regulatoryAPI;
    }

    public function submitTrialData(): void {
        $trialData = $this->clinicalTrialSystem->getTrialData();
        $this->regulatoryAPI->uploadDataToRegulator($trialData);
    }
}

// Usage
$clinicalSystem1 = new ClinicalTrialSystem("Test Small Molecule 01");
$clinicalSystem2 = new ClinicalTrialSystem("Test Small Molecule 02");
$regulatoryAPI = new RegulatoryAPI();

$adapter1 = new RegulatoryAdapter($clinicalSystem1, $regulatoryAPI);
$adapter1->submitTrialData();

$adapter2 = new RegulatoryAdapter($clinicalSystem2, $regulatoryAPI);
$adapter2->submitTrialData();

?>

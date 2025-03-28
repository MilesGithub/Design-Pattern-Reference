// Adaptee: Clinical Trial System
class ClinicalTrialSystem {
    private String trialData;

    public ClinicalTrialSystem(String drugName) {
        this.trialData = drugName + " clinical trial data";
    }

    public String getTrialData() {
        return trialData;
    }
}

// Target: Regulatory API
class RegulatoryAPI {
    public void uploadDataToRegulator(String data) {
        System.out.println("Uploading the following data to regulatory authorities: " + data);
    }
}

// Adapter: Bridges ClinicalTrialSystem (Adaptee) with RegulatoryAPI (Target)
class RegulatoryAdapter {
    private ClinicalTrialSystem clinicalTrialSystem;
    private RegulatoryAPI regulatoryAPI;

    public RegulatoryAdapter(ClinicalTrialSystem clinicalTrialSystem, RegulatoryAPI regulatoryAPI) {
        this.clinicalTrialSystem = clinicalTrialSystem;
        this.regulatoryAPI = regulatoryAPI;
    }

    public void submitTrialData() {
        String trialData = clinicalTrialSystem.getTrialData();
        regulatoryAPI.uploadDataToRegulator(trialData);
    }
}

// Client Code
public class Main {
    public static void main(String[] args) {
        ClinicalTrialSystem clinicalSystem1 = new ClinicalTrialSystem("Test Small Molecule 01");
        ClinicalTrialSystem clinicalSystem2 = new ClinicalTrialSystem("Test Small Molecule 02");
        RegulatoryAPI regulatoryAPI = new RegulatoryAPI();

        RegulatoryAdapter adapter1 = new RegulatoryAdapter(clinicalSystem1, regulatoryAPI);
        adapter1.submitTrialData();

        RegulatoryAdapter adapter2 = new RegulatoryAdapter(clinicalSystem2, regulatoryAPI);
        adapter2.submitTrialData();
    }
}

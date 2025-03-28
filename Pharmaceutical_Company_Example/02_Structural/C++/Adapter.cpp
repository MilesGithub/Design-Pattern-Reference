#include <iostream>
#include <string>

// Adaptee: ClinicalTrialSystem
class ClinicalTrialSystem {
public:
  ClinicalTrialSystem(const std::string& drug_name) 
    : trial_data(drug_name + " clinical trial data") {}
  
  std::string get_trial_data() const {
    return trial_data;
  }
  
private:
  std::string trial_data;
};

// Target: RegulatoryAPI
class RegulatoryAPI {
public:
  void upload_data_to_regulator(const std::string& data) {
    std::cout << "Uploading the following data to regulatory authorities: " << data << std::endl;
  }
};

// Adapter: RegulatoryAdapter
class RegulatoryAdapter {
public:
  RegulatoryAdapter(ClinicalTrialSystem* clinical_trial_system, RegulatoryAPI* regulatory_api)
    : clinical_trial_system(clinical_trial_system), regulatory_api(regulatory_api) {}
  
  void submit_trial_data() {
    std::string trial_data = clinical_trial_system->get_trial_data();
    regulatory_api->upload_data_to_regulator(trial_data);
  }
  
private:
  ClinicalTrialSystem* clinical_trial_system;
  RegulatoryAPI* regulatory_api;
};

int main() {
  // Creating clinical trial systems for different drugs
  ClinicalTrialSystem clinical_system_1("Test Small Molecule 01");
  ClinicalTrialSystem clinical_system_2("Test Small Molecule 02");
  
  // Creating the Regulatory API instance
  RegulatoryAPI regulatory_api;
  
  // Adapter for the first clinical trial system
  RegulatoryAdapter adapter_1(&clinical_system_1, &regulatory_api);
  adapter_1.submit_trial_data();
  
  // Adapter for the second clinical trial system
  RegulatoryAdapter adapter_2(&clinical_system_2, &regulatory_api);
  adapter_2.submit_trial_data();
  
  return 0;
}

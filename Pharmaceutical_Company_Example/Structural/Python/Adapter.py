# Adaptee
class ClinicalTrialSystem:
    def __init__(self, drug_name):
        self.trial_data = f"{drug_name} clinical trial data"

    def get_trial_data(self):
        return self.trial_data


# Target
class RegulatoryAPI:
    def upload_data_to_regulator(self, data):
        print(f"Uploading the following data to regulatory authorities: {data}")


# Adapter to bridge between ClinicalTrialSystem (Adaptee) and RegulatoryAPI (Target)
class RegulatoryAdapter:
    def __init__(self, clinical_trial_system, regulatory_api):
        self.clinical_trial_system = clinical_trial_system
        self.regulatory_api = regulatory_api

    def submit_trial_data(self):
        trial_data = self.clinical_trial_system.get_trial_data()
        self.regulatory_api.upload_data_to_regulator(trial_data)


clinical_system_1 = ClinicalTrialSystem("Test Small Molecule 01")
clinical_system_2 = ClinicalTrialSystem("Test Small Molecule 02")
regulatory_api = RegulatoryAPI()

adapter_1 = RegulatoryAdapter(clinical_system_1, regulatory_api)
adapter_1.submit_trial_data()

adapter_2 = RegulatoryAdapter(clinical_system_2, regulatory_api)
adapter_2.submit_trial_data()

# Prototype
class RegulatoryDocumentPrototype:
    def __init__(self, drug_name, document_type, clinical_trial_data, safety_report, manufacturing_data):
        self.drug_name = drug_name
        self.document_type = document_type
        self.clinical_trial_data = clinical_trial_data
        self.safety_report = safety_report
        self.manufacturing_data = manufacturing_data

    def clone_document(self, new_drug_name):
        # Create a cloned document with a new drug name but same data as the original
        return RegulatoryDocumentPrototype(
            drug_name=new_drug_name,
            document_type=self.document_type,
            clinical_trial_data=self.clinical_trial_data,
            safety_report=self.safety_report,
            manufacturing_data=self.manufacturing_data
        )

    def show_document(self):
        print(f"Regulatory Document for: {self.drug_name}\n"
              f"Document Type: {self.document_type}\n"
              f"Clinical Trial Data: {self.clinical_trial_data}\n"
              f"Safety Report: {self.safety_report}\n"
              f"Manufacturing Data: {self.manufacturing_data}\n")

# Create prototypes
vaccine_prototype = RegulatoryDocumentPrototype(
    drug_name="Vaccine Prototype",
    document_type="Vaccine Regulatory Document",
    clinical_trial_data="Standard vaccine clinical trial data",
    safety_report="Standard vaccine safety report",
    manufacturing_data="Standard vaccine manufacturing data"
)

small_molecule_prototype = RegulatoryDocumentPrototype(
    drug_name="Small-Molecule Prototype",
    document_type="Small-Molecule Regulatory Document",
    clinical_trial_data="Standard small-molecule clinical trial data",
    safety_report="Standard small-molecule safety report",
    manufacturing_data="Standard small-molecule manufacturing data"
)

biologics_prototype = RegulatoryDocumentPrototype(
    drug_name="Biologics Prototype",
    document_type="Biologics Regulatory Document",
    clinical_trial_data="Standard biologics clinical trial data",
    safety_report="Standard biologics safety report",
    manufacturing_data="Standard biologics manufacturing data"
)

# Clone the vaccine prototype for a new vaccine
new_vaccine_document = vaccine_prototype.clone_document("Test Vaccine 01")
new_vaccine_document.show_document()

# Clone the small-molecule prototype for a new drug
new_small_molecule_document = small_molecule_prototype.clone_document("Test Small Molecule 01")
new_small_molecule_document.show_document()

# Clone the biologics prototype for a new biologic drug
new_biologics_document = biologics_prototype.clone_document("Test Monoclonal Antibody 01")
new_biologics_document.show_document()

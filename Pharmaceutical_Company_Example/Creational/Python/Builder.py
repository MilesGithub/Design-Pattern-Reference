# Product
class RegulatoryDocument:
    def __init__(self, drug_name):
        self.drug_name = drug_name
        self.clinical_trial_data = None
        self.safety_report = None
        self.manufacturing_data = None

    def show_document(self):
        print(f"Regulatory Document for: {self.drug_name}\n"
              f"Clinical Trial Data: {self.clinical_trial_data}\n"
              f"Safety Report: {self.safety_report}\n"
              f"Manufacturing Data: {self.manufacturing_data}\n")

# Abstract Builder
class RegulatoryDocumentBuilder:
    def __init__(self, drug_name):
        self.document = RegulatoryDocument(drug_name)

    def add_clinical_trial_data(self):
        raise NotImplementedError("This method must be overridden by a concrete builder")

    def add_safety_report(self):
        raise NotImplementedError("This method must be overridden by a concrete builder")

    def add_manufacturing_data(self):
        raise NotImplementedError("This method must be overridden by a concrete builder")

    def get_document(self):
        return self.document

# Concrete Builder for Vaccines
class VaccineDocumentBuilder(RegulatoryDocumentBuilder):
    def add_clinical_trial_data(self):
        self.document.clinical_trial_data = "Vaccine clinical trial data"

    def add_safety_report(self):
        self.document.safety_report = "Vaccine safety report"

    def add_manufacturing_data(self):
        self.document.manufacturing_data = "Vaccine manufacturing data"

# Concrete Builder for Small-Molecule Drugs
class SmallMoleculeDocumentBuilder(RegulatoryDocumentBuilder):
    def add_clinical_trial_data(self):
        self.document.clinical_trial_data = "Small-molecule clinical trial data"

    def add_safety_report(self):
        self.document.safety_report = "Small-molecule safety report"

    def add_manufacturing_data(self):
        self.document.manufacturing_data = "Small-molecule manufacturing data"

# Concrete Builder for Biologics
class BiologicsDocumentBuilder(RegulatoryDocumentBuilder):
    def add_clinical_trial_data(self):
        self.document.clinical_trial_data = "Biologics clinical trial data"

    def add_safety_report(self):
        self.document.safety_report = "Biologics safety report"

    def add_manufacturing_data(self):
        self.document.manufacturing_data = "Biologics manufacturing data"

# Director: Manages the building process
class RegulatoryDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_document(self):
        self.builder.add_clinical_trial_data()
        self.builder.add_safety_report()
        self.builder.add_manufacturing_data()

    def get_document(self):
        return self.builder.get_document()

# Create a director for a Vaccine regulatory document
vaccine_builder = VaccineDocumentBuilder("Test Vaccine 01")
director = RegulatoryDirector(vaccine_builder)
director.construct_document()
vaccine_doc = director.get_document()
vaccine_doc.show_document()

# Create a director for a Small-Molecule regulatory document
small_molecule_builder = SmallMoleculeDocumentBuilder("Test Small Molecule 01")
director = RegulatoryDirector(small_molecule_builder)
director.construct_document()
small_molecule_doc = director.get_document()
small_molecule_doc.show_document()

# Create a director for a Biologics regulatory document
biologics_builder = BiologicsDocumentBuilder("Test Monoclonal Antibody 01")
director = RegulatoryDirector(biologics_builder)
director.construct_document()
biologics_doc = director.get_document()
biologics_doc.show_document()

# Product
class RegulatoryDocument:
    def __init__(self, drug_name, document_type):
        self.drug_name = drug_name
        self.document_type = document_type

    def show_document(self):
        print(f"Regulatory Document for: {self.drug_name}\n"
              f"Type of Document: {self.document_type}\n")

# Abstract Creator
class RegulatoryDocumentFactory:
    def create_document(self, drug_name):
        raise NotImplementedError("This method must be overridden by a concrete factory!")

# Concrete Creator for Vaccine Documents
class VaccineDocumentFactory(RegulatoryDocumentFactory):
    def create_document(self, drug_name):
        return RegulatoryDocument(drug_name, "Vaccine Regulatory Document")

# Concrete Creator for Small-Molecule Documents
class SmallMoleculeDocumentFactory(RegulatoryDocumentFactory):
    def create_document(self, drug_name):
        return RegulatoryDocument(drug_name, "Small-Molecule Regulatory Document")

# Concrete Creator for Biologics Documents
class BiologicsDocumentFactory(RegulatoryDocumentFactory):
    def create_document(self, drug_name):
        return RegulatoryDocument(drug_name, "Biologics Regulatory Document")

def process_document(factory, drug_name):
    document = factory.create_document(drug_name)
    document.show_document()

vaccine_factory = VaccineDocumentFactory()
process_document(vaccine_factory, "Test Vaccine 01")

small_molecule_factory = SmallMoleculeDocumentFactory()
process_document(small_molecule_factory, "Test Small Molecule 01")

biologics_factory = BiologicsDocumentFactory()
process_document(biologics_factory, "Test Monoclonal Antibody 01")

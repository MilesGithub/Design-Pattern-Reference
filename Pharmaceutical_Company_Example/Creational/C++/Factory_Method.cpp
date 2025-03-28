#include <iostream>
#include <string>
#include <memory>

// Product
class RegulatoryDocument {
public:
  RegulatoryDocument(const std::string& drug_name, const std::string& document_type)
    : drug_name(drug_name), document_type(document_type) {}
  
  void show_document() const {
    std::cout << "Regulatory Document for: " << drug_name << "\n"
              << "Type of Document: " << document_type << "\n";
  }
  
private:
  std::string drug_name;
  std::string document_type;
};

// Abstract Creator
class RegulatoryDocumentFactory {
public:
  virtual ~RegulatoryDocumentFactory() = default;
  
  virtual std::unique_ptr<RegulatoryDocument> create_document(const std::string& drug_name) = 0;
};

// Concrete Creator for Vaccine Documents
class VaccineDocumentFactory : public RegulatoryDocumentFactory {
public:
  std::unique_ptr<RegulatoryDocument> create_document(const std::string& drug_name) override {
    return std::make_unique<RegulatoryDocument>(drug_name, "Vaccine Regulatory Document");
  }
};

// Concrete Creator for Small-Molecule Documents
class SmallMoleculeDocumentFactory : public RegulatoryDocumentFactory {
public:
  std::unique_ptr<RegulatoryDocument> create_document(const std::string& drug_name) override {
    return std::make_unique<RegulatoryDocument>(drug_name, "Small-Molecule Regulatory Document");
  }
};

// Concrete Creator for Biologics Documents
class BiologicsDocumentFactory : public RegulatoryDocumentFactory {
public:
  std::unique_ptr<RegulatoryDocument> create_document(const std::string& drug_name) override {
    return std::make_unique<RegulatoryDocument>(drug_name, "Biologics Regulatory Document");
  }
};

void process_document(std::unique_ptr<RegulatoryDocumentFactory>& factory, const std::string& drug_name) {
  auto document = factory->create_document(drug_name);
  document->show_document();
}

int main() {
  // Create factories
  std::unique_ptr<RegulatoryDocumentFactory> vaccine_factory = std::make_unique<VaccineDocumentFactory>();
  process_document(vaccine_factory, "Test Vaccine 01");
  
  std::unique_ptr<RegulatoryDocumentFactory> small_molecule_factory = std::make_unique<SmallMoleculeDocumentFactory>();
  process_document(small_molecule_factory, "Test Small Molecule 01");
  
  std::unique_ptr<RegulatoryDocumentFactory> biologics_factory = std::make_unique<BiologicsDocumentFactory>();
  process_document(biologics_factory, "Test Monoclonal Antibody 01");
  
  return 0;
}

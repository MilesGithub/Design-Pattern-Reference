#include <iostream>
#include <string>
#include <memory>

// Prototype
class RegulatoryDocumentPrototype {
public:
  RegulatoryDocumentPrototype(const std::string& drug_name, const std::string& document_type,
                              const std::string& clinical_trial_data, const std::string& safety_report,
                              const std::string& manufacturing_data)
    : drug_name(drug_name), document_type(document_type), clinical_trial_data(clinical_trial_data),
      safety_report(safety_report), manufacturing_data(manufacturing_data) {}
  
  // Clone method: creates a copy of the original document with a new drug name
  std::unique_ptr<RegulatoryDocumentPrototype> clone_document(const std::string& new_drug_name) const {
    return std::make_unique<RegulatoryDocumentPrototype>(
      new_drug_name, document_type, clinical_trial_data, safety_report, manufacturing_data);
  }
  
  void show_document() const {
    std::cout << "Regulatory Document for: " << drug_name << "\n"
              << "Document Type: " << document_type << "\n"
              << "Clinical Trial Data: " << clinical_trial_data << "\n"
              << "Safety Report: " << safety_report << "\n"
              << "Manufacturing Data: " << manufacturing_data << "\n";
  }
  
private:
  std::string drug_name;
  std::string document_type;
  std::string clinical_trial_data;
  std::string safety_report;
  std::string manufacturing_data;
};

int main() {
  // Create prototypes
  std::unique_ptr<RegulatoryDocumentPrototype> vaccine_prototype = std::make_unique<RegulatoryDocumentPrototype>(
    "Vaccine Prototype", "Vaccine Regulatory Document", "Standard vaccine clinical trial data",
    "Standard vaccine safety report", "Standard vaccine manufacturing data");
  
  std::unique_ptr<RegulatoryDocumentPrototype> small_molecule_prototype = std::make_unique<RegulatoryDocumentPrototype>(
    "Small-Molecule Prototype", "Small-Molecule Regulatory Document", "Standard small-molecule clinical trial data",
    "Standard small-molecule safety report", "Standard small-molecule manufacturing data");
  
  std::unique_ptr<RegulatoryDocumentPrototype> biologics_prototype = std::make_unique<RegulatoryDocumentPrototype>(
    "Biologics Prototype", "Biologics Regulatory Document", "Standard biologics clinical trial data",
    "Standard biologics safety report", "Standard biologics manufacturing data");
  
  // Clone the vaccine prototype for a new vaccine
  auto new_vaccine_document = vaccine_prototype->clone_document("Test Vaccine 01");
  new_vaccine_document->show_document();
  
  // Clone the small-molecule prototype for a new drug
  auto new_small_molecule_document = small_molecule_prototype->clone_document("Test Small Molecule 01");
  new_small_molecule_document->show_document();
  
  // Clone the biologics prototype for a new biologic drug
  auto new_biologics_document = biologics_prototype->clone_document("Test Monoclonal Antibody 01");
  new_biologics_document->show_document();
  
  return 0;
}

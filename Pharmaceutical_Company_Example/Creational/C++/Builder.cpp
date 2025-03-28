#include <iostream>
#include <string>
#include <memory>

// Product
class RegulatoryDocument {
public:
  explicit RegulatoryDocument(const std::string& drug_name) 
    : drug_name(drug_name), clinical_trial_data(""), safety_report(""), manufacturing_data("") {}
  
  void show_document() const {
    std::cout << "Regulatory Document for: " << drug_name << "\n"
              << "Clinical Trial Data: " << clinical_trial_data << "\n"
              << "Safety Report: " << safety_report << "\n"
              << "Manufacturing Data: " << manufacturing_data << "\n";
  }
  
  void set_clinical_trial_data(const std::string& data) { clinical_trial_data = data; }
  void set_safety_report(const std::string& report) { safety_report = report; }
  void set_manufacturing_data(const std::string& data) { manufacturing_data = data; }
  
private:
  std::string drug_name;
  std::string clinical_trial_data;
  std::string safety_report;
  std::string manufacturing_data;
};

// Abstract Builder
class RegulatoryDocumentBuilder {
public:
  explicit RegulatoryDocumentBuilder(const std::string& drug_name)
    : document(drug_name) {}
  
  virtual ~RegulatoryDocumentBuilder() = default;
  
  virtual void add_clinical_trial_data() = 0;
  virtual void add_safety_report() = 0;
  virtual void add_manufacturing_data() = 0;
  
  RegulatoryDocument* get_document() {
    return &document;
  }
  
protected:
  RegulatoryDocument document;
};

// Concrete Builder for Vaccines
class VaccineDocumentBuilder : public RegulatoryDocumentBuilder {
public:
  explicit VaccineDocumentBuilder(const std::string& drug_name) 
    : RegulatoryDocumentBuilder(drug_name) {}
  
  void add_clinical_trial_data() override {
    document.set_clinical_trial_data("Vaccine clinical trial data");
  }
  
  void add_safety_report() override {
    document.set_safety_report("Vaccine safety report");
  }
  
  void add_manufacturing_data() override {
    document.set_manufacturing_data("Vaccine manufacturing data");
  }
};

// Concrete Builder for Small-Molecule Drugs
class SmallMoleculeDocumentBuilder : public RegulatoryDocumentBuilder {
public:
  explicit SmallMoleculeDocumentBuilder(const std::string& drug_name) 
    : RegulatoryDocumentBuilder(drug_name) {}
  
  void add_clinical_trial_data() override {
    document.set_clinical_trial_data("Small-molecule clinical trial data");
  }
  
  void add_safety_report() override {
    document.set_safety_report("Small-molecule safety report");
  }
  
  void add_manufacturing_data() override {
    document.set_manufacturing_data("Small-molecule manufacturing data");
  }
};

// Concrete Builder for Biologics
class BiologicsDocumentBuilder : public RegulatoryDocumentBuilder {
public:
  explicit BiologicsDocumentBuilder(const std::string& drug_name) 
    : RegulatoryDocumentBuilder(drug_name) {}
  
  void add_clinical_trial_data() override {
    document.set_clinical_trial_data("Biologics clinical trial data");
  }
  
  void add_safety_report() override {
    document.set_safety_report("Biologics safety report");
  }
  
  void add_manufacturing_data() override {
    document.set_manufacturing_data("Biologics manufacturing data");
  }
};

// Director: Manages the building process
class RegulatoryDirector {
public:
  explicit RegulatoryDirector(std::shared_ptr<RegulatoryDocumentBuilder> builder)
    : builder(std::move(builder)) {}
  
  void construct_document() {
    builder->add_clinical_trial_data();
    builder->add_safety_report();
    builder->add_manufacturing_data();
  }
  
  RegulatoryDocument* get_document() {
    return builder->get_document();
  }
  
private:
  std::shared_ptr<RegulatoryDocumentBuilder> builder;
};

int main() {
  // Vaccine Regulatory Process
  auto vaccine_builder = std::make_shared<VaccineDocumentBuilder>("Test Vaccine 01");
  RegulatoryDirector director(vaccine_builder);
  director.construct_document();
  RegulatoryDocument* vaccine_doc = director.get_document();
  vaccine_doc->show_document();
  
  // Small-Molecule Drug Regulatory Process
  auto small_molecule_builder = std::make_shared<SmallMoleculeDocumentBuilder>("Test Small Molecule 01");
  RegulatoryDirector director2(small_molecule_builder);
  director2.construct_document();
  RegulatoryDocument* small_molecule_doc = director2.get_document();
  small_molecule_doc->show_document();
  
  // Biologics Regulatory Process
  auto biologics_builder = std::make_shared<BiologicsDocumentBuilder>("Test Monoclonal Antibody 01");
  RegulatoryDirector director3(biologics_builder);
  director3.construct_document();
  RegulatoryDocument* biologics_doc = director3.get_document();
  biologics_doc->show_document();
  
  return 0;
}

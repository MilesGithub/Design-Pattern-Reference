#include <iostream>
#include <memory>

// Abstract Factory Interface
class RegulatoryFactory {
public:
  virtual ~RegulatoryFactory() = default;
  virtual class SubmissionForm* create_submission_form() = 0;
  virtual class TestingProtocol* create_testing_protocol() = 0;
};

// Concrete Factory for Vaccines
class VaccineRegulatoryFactory : public RegulatoryFactory {
public:
  class SubmissionForm* create_submission_form() override;
  class TestingProtocol* create_testing_protocol() override;
};

// Concrete Factory for Small-Molecule Drugs
class SmallMoleculeRegulatoryFactory : public RegulatoryFactory {
public:
  class SubmissionForm* create_submission_form() override;
  class TestingProtocol* create_testing_protocol() override;
};

// Concrete Factory for Biologics
class BiologicsRegulatoryFactory : public RegulatoryFactory {
public:
  class SubmissionForm* create_submission_form() override;
  class TestingProtocol* create_testing_protocol() override;
};

// Abstract Product: Submission Form
class SubmissionForm {
public:
  virtual ~SubmissionForm() = default;
  virtual void submit() = 0;
};

// Concrete Product: Vaccine Submission Form
class VaccineSubmissionForm : public SubmissionForm {
public:
  void submit() override {
    std::cout << "Submitting vaccine clinical trial data form." << std::endl;
  }
};

// Concrete Product: Small-Molecule Submission Form
class SmallMoleculeSubmissionForm : public SubmissionForm {
public:
  void submit() override {
    std::cout << "Submitting small-molecule drug trial data form." << std::endl;
  }
};

// Concrete Product: Biologics Submission Form
class BiologicsSubmissionForm : public SubmissionForm {
public:
  void submit() override {
    std::cout << "Submitting biologics clinical trial data form." << std::endl;
  }
};

// Abstract Product: Testing Protocol
class TestingProtocol {
public:
  virtual ~TestingProtocol() = default;
  virtual void run_tests() = 0;
};

// Concrete Product: Vaccine Testing Protocol
class VaccineTestingProtocol : public TestingProtocol {
public:
  void run_tests() override {
    std::cout << "Running tests for vaccines." << std::endl;
  }
};

// Concrete Product: Small-Molecule Testing Protocol
class SmallMoleculeTestingProtocol : public TestingProtocol {
public:
  void run_tests() override {
    std::cout << "Running tests for small-molecule drugs." << std::endl;
  }
};

// Concrete Product: Biologics Testing Protocol
class BiologicsTestingProtocol : public TestingProtocol {
public:
  void run_tests() override {
    std::cout << "Running tests for biologics." << std::endl;
  }
};

// Process Regulatory Approval
void process_regulatory_approval(RegulatoryFactory* factory) {
  std::unique_ptr<SubmissionForm> submission_form(factory->create_submission_form());
  std::unique_ptr<TestingProtocol> testing_protocol(factory->create_testing_protocol());
  
  submission_form->submit();
  testing_protocol->run_tests();
}

int main() {
  // Vaccine Regulatory Process
  VaccineRegulatoryFactory vaccine_factory;
  process_regulatory_approval(&vaccine_factory);
  
  // Small-Molecule Drug Regulatory Process
  SmallMoleculeRegulatoryFactory small_molecule_factory;
  process_regulatory_approval(&small_molecule_factory);
  
  // Biologics Regulatory Process
  BiologicsRegulatoryFactory biologics_factory;
  process_regulatory_approval(&biologics_factory);
  
  return 0;
}

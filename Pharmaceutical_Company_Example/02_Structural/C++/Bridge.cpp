#include <iostream>
#include <memory>
using namespace std;

// Abstract Implementation
class RegulatoryImplementation {
public:
  virtual void submit() = 0;
  virtual void approve() = 0;
  virtual ~RegulatoryImplementation() {}
};

// Abstraction
class RegulatoryProcess {
protected:
  shared_ptr<RegulatoryImplementation> implementation;
  
public:
  RegulatoryProcess(shared_ptr<RegulatoryImplementation> impl) : implementation(impl) {}
  
  void submit() {
    implementation->submit();
  }
  
  void approve() {
    implementation->approve();
  }
};

// Concrete implementation for Vaccine
class VaccineProcess : public RegulatoryImplementation {
public:
  void submit() override {
    cout << "Submitting vaccine clinical trial data..." << endl;
  }
  
  void approve() override {
    cout << "Vaccine regulatory approval granted." << endl;
  }
};

// Concrete implementation for Small-Molecule Drugs
class SmallMoleculeDrugProcess : public RegulatoryImplementation {
public:
  void submit() override {
    cout << "Submitting small-molecule clinical trial data..." << endl;
  }
  
  void approve() override {
    cout << "Small-molecule regulatory approval granted." << endl;
  }
};

// Concrete implementation for Biologics
class BiologicsProcess : public RegulatoryImplementation {
public:
  void submit() override {
    cout << "Submitting biologics clinical trial data..." << endl;
  }
  
  void approve() override {
    cout << "Biologics regulatory approval granted." << endl;
  }
};

// Main
int main() {
  auto preclinical_small_molecule = make_shared<RegulatoryProcess>(make_shared<SmallMoleculeDrugProcess>());
  preclinical_small_molecule->submit();
  preclinical_small_molecule->approve();
  
  auto clinical_biologics = make_shared<RegulatoryProcess>(make_shared<BiologicsProcess>());
  clinical_biologics->submit();
  clinical_biologics->approve();
  
  auto clinical_vaccine = make_shared<RegulatoryProcess>(make_shared<VaccineProcess>());
  clinical_vaccine->submit();
  clinical_vaccine->approve();
  
  return 0;
}

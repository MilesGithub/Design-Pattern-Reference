#include <iostream>
#include <memory>
#include <string>

using namespace std;

// Mediator Interface
class Mediator {
public:
  virtual void notify(const string& sender, const string& event) = 0;
  virtual ~Mediator() = default;
};

// Concrete Mediator
class RegulatoryMediator : public Mediator {
private:
  class ClinicalTrials* clinical_trials;
  class QualityAssurance* quality_assurance;
  class RegulatoryAffairs* regulatory_affairs;
  class LegalDepartment* legal;
  
public:
  void setClinicalTrials(ClinicalTrials* ct) { clinical_trials = ct; }
  void setQualityAssurance(QualityAssurance* qa) { quality_assurance = qa; }
  void setRegulatoryAffairs(RegulatoryAffairs* ra) { regulatory_affairs = ra; }
  void setLegalDepartment(LegalDepartment* ld) { legal = ld; }
  
  void notify(const string& sender, const string& event) override;
};

// Department Interfaces
class Department {
protected:
  Mediator* mediator;
public:
  Department(Mediator* mediator) : mediator(mediator) {}
  virtual void completeTask() = 0;
  virtual ~Department() = default;
};

// Concrete Department: Clinical Trials
class ClinicalTrials : public Department {
public:
  ClinicalTrials(Mediator* mediator) : Department(mediator) {}
  
  void runTrials() {
    cout << "Clinical Trials: Running clinical trials..." << endl;
    mediator->notify("ClinicalTrials", "Clinical Trial Completed");
  }
  
  void completeTask() override {}
};

// Concrete Department: Quality Assurance
class QualityAssurance : public Department {
public:
  QualityAssurance(Mediator* mediator) : Department(mediator) {}
  
  void checkQuality() {
    cout << "Quality Assurance: Checking product quality..." << endl;
    mediator->notify("QualityAssurance", "Quality Check Completed");
  }
  
  void completeTask() override {}
};

// Concrete Department: Regulatory Affairs
class RegulatoryAffairs : public Department {
public:
  RegulatoryAffairs(Mediator* mediator) : Department(mediator) {}
  
  void prepareDocuments() {
    cout << "Regulatory Affairs: Preparing regulatory documents..." << endl;
    mediator->notify("RegulatoryAffairs", "Documents Prepared");
  }
  
  void completeTask() override {}
};

// Concrete Department: Legal Department
class LegalDepartment : public Department {
public:
  LegalDepartment(Mediator* mediator) : Department(mediator) {}
  
  void reviewDocuments() {
    cout << "Legal Department: Reviewing regulatory documents..." << endl;
    mediator->notify("LegalDepartment", "Legal Review Completed");
  }
  
  void completeTask() override {}
};

// Concrete Mediator Method Implementation
void RegulatoryMediator::notify(const string& sender, const string& event) {
  if (event == "Clinical Trial Completed") {
    cout << "Mediator: Clinical Trial completed. Notifying Quality Assurance." << endl;
    if (quality_assurance) {
      quality_assurance->checkQuality();
    }
  } else if (event == "Quality Check Completed") {
    cout << "Mediator: Quality Check completed. Notifying Regulatory Affairs." << endl;
    if (regulatory_affairs) {
      regulatory_affairs->prepareDocuments();
    }
  } else if (event == "Documents Prepared") {
    cout << "Mediator: Documents prepared. Notifying Legal Department." << endl;
    if (legal) {
      legal->reviewDocuments();
    }
  } else if (event == "Legal Review Completed") {
    cout << "Mediator: Legal Review completed. Drug is ready for final approval." << endl;
  }
}

int main() {
  // Create Mediator
  auto mediator = make_shared<RegulatoryMediator>();
  
  // Create Departments
  auto clinical_trials = make_shared<ClinicalTrials>(mediator.get());
  auto quality_assurance = make_shared<QualityAssurance>(mediator.get());
  auto regulatory_affairs = make_shared<RegulatoryAffairs>(mediator.get());
  auto legal = make_shared<LegalDepartment>(mediator.get());
  
  // Set Departments in the Mediator
  mediator->setClinicalTrials(clinical_trials.get());
  mediator->setQualityAssurance(quality_assurance.get());
  mediator->setRegulatoryAffairs(regulatory_affairs.get());
  mediator->setLegalDepartment(legal.get());
  
  // Run process
  clinical_trials->runTrials();
  
  return 0;
}

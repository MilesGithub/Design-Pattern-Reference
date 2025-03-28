#include <iostream>
#include <vector>
#include <string>

// Observer Interface
class Observer {
public:
  virtual void update(const std::string& state) = 0;
  virtual ~Observer() = default;
};

// Subject
class DrugApprovalProcess {
private:
  std::vector<Observer*> observers;
  std::string state;
  
public:
  void attach_observer(Observer* observer) {
    observers.push_back(observer);
  }
  
  void detach_observer(Observer* observer) {
    auto it = std::remove(observers.begin(), observers.end(), observer);
    observers.erase(it, observers.end());
  }
  
  void notify_observers() {
    std::cout << "DrugApprovalProcess: Notifying observers about state change to: " << state << std::endl;
    for (auto& observer : observers) {
      observer->update(state);
    }
  }
  
  void set_state(const std::string& new_state) {
    state = new_state;
    std::cout << "DrugApprovalProcess: State changed to: " << state << std::endl;
    notify_observers();
  }
};

// Concrete Observer: Clinical Trials Department
class ClinicalTrials : public Observer {
public:
  void update(const std::string& state) override {
    std::cout << "Clinical Trials Department: Notified about state change to: " << state << std::endl;
  }
};

// Concrete Observer: Quality Assurance Department
class QualityAssurance : public Observer {
public:
  void update(const std::string& state) override {
    std::cout << "Quality Assurance Department: Notified about state change to: " << state << std::endl;
  }
};

// Concrete Observer: Legal Department
class LegalDepartment : public Observer {
public:
  void update(const std::string& state) override {
    std::cout << "Legal Department: Notified about state change to: " << state << std::endl;
  }
};

// Concrete Observer: Regulatory Affairs Department
class RegulatoryAffairs : public Observer {
public:
  void update(const std::string& state) override {
    std::cout << "Regulatory Affairs Department: Notified about state change to: " << state << std::endl;
  }
};

int main() {
  // Create the DrugApprovalProcess (Subject)
  DrugApprovalProcess drug_approval_process;
  
  // Create observers
  ClinicalTrials clinical_trials;
  QualityAssurance quality_assurance;
  LegalDepartment legal;
  RegulatoryAffairs regulatory_affairs;
  
  // Attach observers to the subject
  drug_approval_process.attach_observer(&clinical_trials);
  drug_approval_process.attach_observer(&quality_assurance);
  drug_approval_process.attach_observer(&legal);
  drug_approval_process.attach_observer(&regulatory_affairs);
  
  // Simulate state changes and notify observers
  drug_approval_process.set_state("Clinical Trial Started");
  drug_approval_process.set_state("Clinical Trial Completed");
  drug_approval_process.set_state("Quality Check in Progress");
  drug_approval_process.set_state("Under Regulatory Review");
  drug_approval_process.set_state("Approved");
  
  return 0;
}

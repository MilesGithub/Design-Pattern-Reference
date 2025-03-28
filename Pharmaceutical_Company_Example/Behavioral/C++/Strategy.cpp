#include <iostream>
#include <string>

// Strategy Interface
class RegulatoryStrategy {
public:
  virtual void approve_application(const std::string& drug_name) = 0;
  virtual ~RegulatoryStrategy() = default;
};

// Concrete Strategy: Standard Approval
class StandardApprovalStrategy : public RegulatoryStrategy {
public:
  void approve_application(const std::string& drug_name) override {
    std::cout << "Applying Standard Approval Process for drug: " << drug_name << std::endl;
    std::cout << drug_name << " has been approved using the Standard Approval Strategy." << std::endl;
  }
};

// Concrete Strategy: Accelerated Approval
class AcceleratedApprovalStrategy : public RegulatoryStrategy {
public:
  void approve_application(const std::string& drug_name) override {
    std::cout << "Applying Accelerated Approval Process for drug: " << drug_name << std::endl;
    std::cout << drug_name << " has been approved using the Accelerated Approval Strategy." << std::endl;
  }
};

// Context
class DrugApprovalContext {
private:
  RegulatoryStrategy* strategy;
  
public:
  DrugApprovalContext(RegulatoryStrategy* strategy) : strategy(strategy) {}
  
  void set_strategy(RegulatoryStrategy* new_strategy) {
    strategy = new_strategy;
  }
  
  void approve_drug(const std::string& drug_name) {
    strategy->approve_application(drug_name);
  }
};

// Example Usage
int main() {
  // Create Context with Standard Approval Strategy
  DrugApprovalContext approval_context(new StandardApprovalStrategy());
  
  // Use Standard Approval Strategy
  approval_context.approve_drug("Test Small Molecule 01");
  
  // Change to Accelerated Approval Strategy
  approval_context.set_strategy(new AcceleratedApprovalStrategy());
  approval_context.approve_drug("Test Small Molecule 02");
  
  return 0;
}

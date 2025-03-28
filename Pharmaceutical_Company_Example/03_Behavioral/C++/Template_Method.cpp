#include <iostream>
#include <string>

// Abstract Class with Template Method
class RegulatoryProcess {
public:
  void execute_process(const std::string& drug_name) {
    std::cout << "Starting the regulatory process for drug: " << drug_name << std::endl;
    perform_evaluation(drug_name);
    perform_approval(drug_name);
    finalize_process(drug_name);
    std::cout << "Regulatory process completed for drug: " << drug_name << std::endl;
  }
  
  // Abstract Methods
  virtual void perform_evaluation(const std::string& drug_name) = 0;
  virtual void perform_approval(const std::string& drug_name) = 0;
  
  // Final Method
  void finalize_process(const std::string& drug_name) {
    std::cout << "Finalizing process for drug: " << drug_name << std::endl;
  }
  
  virtual ~RegulatoryProcess() = default;
};

// Concrete Class: Standard Approval Process
class StandardApprovalProcess : public RegulatoryProcess {
public:
  void perform_evaluation(const std::string& drug_name) override {
    std::cout << "Evaluating drug: " << drug_name << " using Standard Evaluation." << std::endl;
  }
  
  void perform_approval(const std::string& drug_name) override {
    std::cout << "Approving drug: " << drug_name << " using Standard Approval Process." << std::endl;
  }
};

// Concrete Class: Accelerated Approval Process
class AcceleratedApprovalProcess : public RegulatoryProcess {
public:
  void perform_evaluation(const std::string& drug_name) override {
    std::cout << "Evaluating drug: " << drug_name << " using Accelerated Evaluation." << std::endl;
  }
  
  void perform_approval(const std::string& drug_name) override {
    std::cout << "Approving drug: " << drug_name << " using Accelerated Approval Process." << std::endl;
  }
};

// Example Usage
int main() {
  // Create instances of the concrete classes
  StandardApprovalProcess standard_process;
  AcceleratedApprovalProcess accelerated_process;
  
  // Execute processes
  standard_process.execute_process("Test Small Molecule 01");
  accelerated_process.execute_process("Test Small Molecule 02");
  
  return 0;
}

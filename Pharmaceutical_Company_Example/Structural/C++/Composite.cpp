#include <iostream>
#include <vector>
#include <string>

// Component
class RegulatoryProcess {
public:
  virtual void execute() = 0;
  virtual ~RegulatoryProcess() = default;
};

// Leaf
class Step : public RegulatoryProcess {
public:
  Step(const std::string& step_name) : step_name(step_name) {}
  
  void execute() override {
    std::cout << "Executing step: " << step_name << std::endl;
  }
  
private:
  std::string step_name;
};

// Composite
class CompositeProcess : public RegulatoryProcess {
public:
  CompositeProcess(const std::string& process_name) : process_name(process_name) {}
  
  void add(RegulatoryProcess* process) {
    children.push_back(process);
  }
  
  void remove(RegulatoryProcess* process) {
    children.erase(std::remove(children.begin(), children.end(), process), children.end());
  }
  
  void execute() override {
    std::cout << "Executing composite process: " << process_name << std::endl;
    for (auto& child : children) {
      child->execute();
    }
  }
  
private:
  std::string process_name;
  std::vector<RegulatoryProcess*> children;
};

int main() {
  // Leaf objects - individual steps
  Step clinical_trial_step("Clinical Trial Approval");
  Step safety_step("Safety Review");
  Step manufacturing_step("Manufacturing Validation");
  
  // Composite processes
  CompositeProcess clinical_process("Clinical Process");
  clinical_process.add(&clinical_trial_step);
  
  CompositeProcess regulatory_process("Regulatory Process");
  regulatory_process.add(&safety_step);
  regulatory_process.add(&manufacturing_step);
  
  CompositeProcess full_approval_process("Full Drug Approval Process");
  full_approval_process.add(&clinical_process);
  full_approval_process.add(&regulatory_process);
  
  // Execute the full approval process
  full_approval_process.execute();
  
  return 0;
}

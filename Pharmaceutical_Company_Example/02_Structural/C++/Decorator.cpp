#include <iostream>
#include <string>

// Base class
class RegulatoryProcess {
public:
  virtual void execute() = 0;
  virtual ~RegulatoryProcess() = default;
};

// Concrete class
class BasicRegulatoryStep : public RegulatoryProcess {
public:
  BasicRegulatoryStep(const std::string& step_name) : step_name(step_name) {}
  
  void execute() override {
    std::cout << "Executing step: " << step_name << std::endl;
  }
  
private:
  std::string step_name;
};

// Decorator Base Class for adding additional features to RegulatoryProcess
class ProcessDecorator : public RegulatoryProcess {
public:
  ProcessDecorator(RegulatoryProcess* decorated_process) : decorated_process(decorated_process) {}
  
  void execute() override {
    decorated_process->execute();
  }
  
protected:
  RegulatoryProcess* decorated_process;
};

// Concrete Decorator - Adds Auditing feature to the regulatory process
class AuditingDecorator : public ProcessDecorator {
public:
  AuditingDecorator(RegulatoryProcess* decorated_process) : ProcessDecorator(decorated_process) {}
  
  void execute() override {
    ProcessDecorator::execute();
    add_audit();
  }
  
private:
  void add_audit() {
    std::cout << "Adding auditing to step." << std::endl;
  }
};

// Concrete Decorator - Adds Documentation requirement to the process
class DocumentationDecorator : public ProcessDecorator {
public:
  DocumentationDecorator(RegulatoryProcess* decorated_process) : ProcessDecorator(decorated_process) {}
  
  void execute() override {
    ProcessDecorator::execute();
    add_documentation();
  }
  
private:
  void add_documentation() {
    std::cout << "Ensuring documentation is complete for step." << std::endl;
  }
};

int main() {
  // Concrete steps
  BasicRegulatoryStep clinical_trial_step("Clinical Trial Approval");
  BasicRegulatoryStep safety_review_step("Safety Review");
  
  // Decorate the clinical trial step with auditing and documentation features
  AuditingDecorator clinical_trial_with_audit(&clinical_trial_step);
  DocumentationDecorator clinical_trial_with_full_features(&clinical_trial_with_audit);
  
  // Decorate the safety review step with documentation only
  DocumentationDecorator safety_review_with_documentation(&safety_review_step);
  
  // Execute both processes
  std::cout << "Executing Clinical Trial Step with Audit and Documentation:" << std::endl;
  clinical_trial_with_full_features.execute();
  
  std::cout << "\nExecuting Safety Review Step with Documentation:" << std::endl;
  safety_review_with_documentation.execute();
  
  return 0;
}

#include <iostream>
#include <string>

// Abstract class for Drug Approval Process
class DrugApprovalProcess {
public:
  virtual void applyForApproval(const std::string& drugName) = 0;
  virtual ~DrugApprovalProcess() = default;
};

// Real class that implements the drug approval process
class RealDrugApprovalProcess : public DrugApprovalProcess {
public:
  void applyForApproval(const std::string& drugName) override {
    std::cout << "Processing approval for drug: " << drugName << std::endl;
  }
};

// Proxy class to control access to the real drug approval process
class DrugApprovalProxy : public DrugApprovalProcess {
private:
  RealDrugApprovalProcess realSubject;
  
public:
  bool checkAuthorization() {
    std::cout << "Checking authorization..." << std::endl;
    return true;  // Return true or false for authorized/unauthorized access
  }
  
  void applyForApproval(const std::string& drugName) override {
    if (checkAuthorization()) {
      realSubject.applyForApproval(drugName);
    } else {
      std::cout << "Unauthorized access" << std::endl;
    }
  }
};

// Function to request approval through the proxy
void requestApproval(DrugApprovalProcess* proxy, const std::string& drugType) {
  std::cout << "\nRequesting approval for " << drugType << "..." << std::endl;
  proxy->applyForApproval(drugType);
}

int main() {
  // Create Proxy instance
  DrugApprovalProxy proxy;
  
  // Request approval for different drug types
  requestApproval(&proxy, "Test Vaccine 01");
  requestApproval(&proxy, "Test Small Molecule 01");
  requestApproval(&proxy, "Test Biologics 01");
  
  return 0;
}

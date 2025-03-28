#include <iostream>
#include <string>
#include <unordered_map>

class RegulatoryApprovalSystem {
public:
  // Method to get the instance of the Singleton class
  static RegulatoryApprovalSystem& get_instance() {
    static RegulatoryApprovalSystem instance;
    return instance;
  }
  
  // Method to add an approval status
  void add_approval(const std::string& drug_name, const std::string& status) {
    approvals[drug_name] = status;
    std::cout << "Added approval status for: " << drug_name << " - Status: " << status << std::endl;
  }
  
  // Method to get the approval status
  void get_status(const std::string& drug_name) {
    if (approvals.find(drug_name) != approvals.end()) {
      std::cout << "Approval status for " << drug_name << " is: " << approvals[drug_name] << std::endl;
    } else {
      std::cout << "No approval status found for " << drug_name << std::endl;
    }
  }
  
  // Method to show all approval statuses
  void show_all_approvals() {
    std::cout << "Current approval statuses:" << std::endl;
    for (const auto& approval : approvals) {
      std::cout << approval.first << " : " << approval.second << std::endl;
    }
  }
  
private:
  // Private constructor to prevent instantiation
  RegulatoryApprovalSystem() {}
  
  // Private copy constructor and assignment operator to ensure the Singleton property
  RegulatoryApprovalSystem(const RegulatoryApprovalSystem&) = delete;
  RegulatoryApprovalSystem& operator=(const RegulatoryApprovalSystem&) = delete;
  
  // Data structure to store approval statuses
  std::unordered_map<std::string, std::string> approvals;
};

int main() {
  // Get the single instance of RegulatoryApprovalSystem
  RegulatoryApprovalSystem& approval_system = RegulatoryApprovalSystem::get_instance();
  
  // Add approvals
  approval_system.add_approval("Test Vaccine 01", "Approved");
  approval_system.add_approval("Test Small Molecule 01", "Under Review");
  approval_system.add_approval("Test Monoclonal Antibody 01", "Approved");
  
  approval_system.get_status("Test Small Molecule 01");
  approval_system.get_status("Test Vaccine 01");
  
  approval_system.show_all_approvals();
  
  // Get another reference to the same instance
  RegulatoryApprovalSystem& approval_system_2 = RegulatoryApprovalSystem::get_instance();
  approval_system_2.add_approval("Test Small Molecule 02", "Pending Review");
  
  // Both references point to the same instance
  approval_system_2.show_all_approvals();
  approval_system.show_all_approvals();
  
  return 0;
}

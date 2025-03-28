#include <iostream>
#include <vector>
#include <unordered_map>
#include <memory>

using namespace std;

// Command Interface
class RegulatoryCommand {
public:
  virtual void execute() = 0;
  virtual ~RegulatoryCommand() = default;
};

// Receiver
class RegulatorySystem {
private:
  unordered_map<string, string> applications;
  
public:
  void submitApplication(const string& drugName) {
    applications[drugName] = "Submitted";
    cout << "Application submitted for: " << drugName << endl;
  }
  
  void approveDrug(const string& drugName) {
    if (applications.find(drugName) != applications.end()) {
      applications[drugName] = "Approved";
      cout << drugName << " approved." << endl;
    } else {
      cout << "No application found for: " << drugName << endl;
    }
  }
  
  void rejectDrug(const string& drugName) {
    if (applications.find(drugName) != applications.end()) {
      applications[drugName] = "Rejected";
      cout << drugName << " rejected." << endl;
    } else {
      cout << "No application found for: " << drugName << endl;
    }
  }
  
  void showStatus(const string& drugName) const {
    auto it = applications.find(drugName);
    if (it != applications.end()) {
      cout << "Current status of " << drugName << ": " << it->second << endl;
    } else {
      cout << "No status found for: " << drugName << endl;
    }
  }
};

// Concrete Command: Submit Drug Application
class SubmitApplicationCommand : public RegulatoryCommand {
private:
  string drugName;
  RegulatorySystem& system;
  
public:
  SubmitApplicationCommand(const string& drugName, RegulatorySystem& system) 
    : drugName(drugName), system(system) {}
  
  void execute() override {
    system.submitApplication(drugName);
  }
};

// Concrete Command: Approve Drug
class ApproveDrugCommand : public RegulatoryCommand {
private:
  string drugName;
  RegulatorySystem& system;
  
public:
  ApproveDrugCommand(const string& drugName, RegulatorySystem& system) 
    : drugName(drugName), system(system) {}
  
  void execute() override {
    system.approveDrug(drugName);
  }
};

// Concrete Command: Reject Drug
class RejectDrugCommand : public RegulatoryCommand {
private:
  string drugName;
  RegulatorySystem& system;
  
public:
  RejectDrugCommand(const string& drugName, RegulatorySystem& system) 
    : drugName(drugName), system(system) {}
  
  void execute() override {
    system.rejectDrug(drugName);
  }
};

// Invoker
class ApprovalSystemInvoker {
private:
  vector<unique_ptr<RegulatoryCommand>> commands;
  
public:
  void addCommand(unique_ptr<RegulatoryCommand> command) {
    commands.push_back(move(command));
  }
  
  void executeCommands() {
    for (auto& command : commands) {
      command->execute();
    }
    commands.clear(); // Clear the command queue after execution
  }
};

int main() {
  // Create Receiver
  RegulatorySystem regulatorySystem;
  
  // Create Invoker
  ApprovalSystemInvoker approvalSystemInvoker;
  
  // Add commands to invoker
  approvalSystemInvoker.addCommand(make_unique<SubmitApplicationCommand>("Test Small Molecule 01", regulatorySystem));
  approvalSystemInvoker.addCommand(make_unique<ApproveDrugCommand>("Test Small Molecule 01", regulatorySystem));
  approvalSystemInvoker.addCommand(make_unique<RejectDrugCommand>("Test Small Molecule 02", regulatorySystem));
  
  // Execute commands
  approvalSystemInvoker.executeCommands();
  
  // Show the status of drugs after executing commands
  regulatorySystem.showStatus("Test Small Molecule 01");
  regulatorySystem.showStatus("Test Small Molecule 02");
  
  return 0;
}

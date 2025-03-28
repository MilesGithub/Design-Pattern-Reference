#include <iostream>
#include <string>

// State interface
class DrugState {
public:
  virtual void proceed_to_next(class DrugApplication& drug_application) = 0;
  virtual std::string get_state_name() const = 0;
  virtual ~DrugState() = default;
};

// Forward declarations of concrete state classes
class SubmittedState;
class ClinicalTrialState;
class UnderReviewState;
class ApprovedState;

// Context class: DrugApplication
class DrugApplication {
private:
  DrugState* state;
  
public:
  DrugApplication(DrugState* initial_state) : state(initial_state) {}
  
  void set_state(DrugState* new_state) {
    state = new_state;
    std::cout << "DrugApplication: State changed to: " << state->get_state_name() << std::endl;
  }
  
  void proceed() {
    state->proceed_to_next(*this);
  }
  
  std::string get_current_state() const {
    return state->get_state_name();
  }
};

// Submitted State
class SubmittedState : public DrugState {
public:
  void proceed_to_next(DrugApplication& drug_application) override {
    std::cout << "Proceeding from Submitted to Clinical Trial..." << std::endl;
    drug_application.set_state(new ClinicalTrialState());
  }
  
  std::string get_state_name() const override {
    return "Submitted";
  }
};

// Clinical Trial State
class ClinicalTrialState : public DrugState {
public:
  void proceed_to_next(DrugApplication& drug_application) override {
    std::cout << "Proceeding from Clinical Trial to Under Review..." << std::endl;
    drug_application.set_state(new UnderReviewState());
  }
  
  std::string get_state_name() const override {
    return "Clinical Trial";
  }
};

// Under Review State
class UnderReviewState : public DrugState {
public:
  void proceed_to_next(DrugApplication& drug_application) override {
    std::cout << "Proceeding from Under Review to Approved..." << std::endl;
    drug_application.set_state(new ApprovedState());
  }
  
  std::string get_state_name() const override {
    return "Under Review";
  }
};

// Approved State
class ApprovedState : public DrugState {
public:
  void proceed_to_next(DrugApplication& drug_application) override {
    std::cout << "The drug has already been approved. No further states." << std::endl;
  }
  
  std::string get_state_name() const override {
    return "Approved";
  }
};

int main() {
  // Initial drug application in "Submitted" state
  DrugApplication drug_application(new SubmittedState());
  
  drug_application.proceed();  // Moves to Clinical Trial
  drug_application.proceed();  // Moves to Under Review
  drug_application.proceed();  // Moves to Approved
  drug_application.proceed();  // Already Approved, no further state
  
  return 0;
}

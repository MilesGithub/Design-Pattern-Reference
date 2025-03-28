#include <iostream>
#include <unordered_map>
#include <memory>

using namespace std;

// Abstract Expression Interface
class RegulatoryExpression {
public:
  virtual bool interpret(const unordered_map<string, bool>& context) const = 0;
  virtual ~RegulatoryExpression() = default;
};

// Concrete Expression: Clinical Trial Passed
class ClinicalTrialPassed : public RegulatoryExpression {
public:
  bool interpret(const unordered_map<string, bool>& context) const override {
    auto it = context.find("clinical_trial_passed");
    return it != context.end() && it->second;
  }
};

// Concrete Expression: Safety Evaluation Passed
class SafetyEvaluationPassed : public RegulatoryExpression {
public:
  bool interpret(const unordered_map<string, bool>& context) const override {
    auto it = context.find("safety_evaluation_passed");
    return it != context.end() && it->second;
  }
};

// Concrete Expression: Manufacturing Approved
class ManufacturingApproved : public RegulatoryExpression {
public:
  bool interpret(const unordered_map<string, bool>& context) const override {
    auto it = context.find("manufacturing_approved");
    return it != context.end() && it->second;
  }
};

// Compound Expression: And Expression (All conditions must be true)
class AndExpression : public RegulatoryExpression {
private:
  shared_ptr<RegulatoryExpression> expr1;
  shared_ptr<RegulatoryExpression> expr2;
  
public:
  AndExpression(shared_ptr<RegulatoryExpression> expr1, shared_ptr<RegulatoryExpression> expr2)
    : expr1(expr1), expr2(expr2) {}
  
  bool interpret(const unordered_map<string, bool>& context) const override {
    return expr1->interpret(context) && expr2->interpret(context);
  }
};

// Compound Expression: Or Expression (At least one condition must be true)
class OrExpression : public RegulatoryExpression {
private:
  shared_ptr<RegulatoryExpression> expr1;
  shared_ptr<RegulatoryExpression> expr2;
  
public:
  OrExpression(shared_ptr<RegulatoryExpression> expr1, shared_ptr<RegulatoryExpression> expr2)
    : expr1(expr1), expr2(expr2) {}
  
  bool interpret(const unordered_map<string, bool>& context) const override {
    return expr1->interpret(context) || expr2->interpret(context);
  }
};

int main() {
  // Context for drug statuses
  unordered_map<string, bool> drug1_context = {
    {"clinical_trial_passed", true},
    {"safety_evaluation_passed", true},
    {"manufacturing_approved", true}
  };
  
  unordered_map<string, bool> drug2_context = {
    {"clinical_trial_passed", true},
    {"safety_evaluation_passed", false},
    {"manufacturing_approved", true}
  };
  
  // Create expressions
  shared_ptr<RegulatoryExpression> clinical_trial_expr = make_shared<ClinicalTrialPassed>();
  shared_ptr<RegulatoryExpression> safety_eval_expr = make_shared<SafetyEvaluationPassed>();
  shared_ptr<RegulatoryExpression> manufacturing_expr = make_shared<ManufacturingApproved>();
  
  // Create approval rule expression using AndExpression
  shared_ptr<RegulatoryExpression> approval_rule_expr = make_shared<AndExpression>(
    clinical_trial_expr,
    make_shared<AndExpression>(safety_eval_expr, manufacturing_expr)
  );
  
  // Check approval status for drugs
  cout << "Test Small Molecule 01 Approval Status: " << approval_rule_expr->interpret(drug1_context) << endl;
  cout << "Test Small Molecule 02 Approval Status: " << approval_rule_expr->interpret(drug2_context) << endl;
  
  return 0;
}

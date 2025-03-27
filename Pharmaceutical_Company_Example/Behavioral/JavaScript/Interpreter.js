// Abstract Expression Interface
class RegulatoryExpression {
  interpret(context) {
    throw new Error("This method should be overridden by concrete expressions!");
  }
}

// Concrete Expression: Clinical Trial Passed
class ClinicalTrialPassed extends RegulatoryExpression {
  interpret(context) {
    return context.clinical_trial_passed || false;
  }
}

// Concrete Expression: Safety Evaluation Passed
class SafetyEvaluationPassed extends RegulatoryExpression {
  interpret(context) {
    return context.safety_evaluation_passed || false;
  }
}

// Concrete Expression: Manufacturing Approved
class ManufacturingApproved extends RegulatoryExpression {
  interpret(context) {
    return context.manufacturing_approved || false;
  }
}

// Compound Expression: And Expression (All conditions must be true)
class AndExpression extends RegulatoryExpression {
  constructor(expr1, expr2) {
    super();
    this.expr1 = expr1;
    this.expr2 = expr2;
  }

  interpret(context) {
    return this.expr1.interpret(context) && this.expr2.interpret(context);
  }
}

// Compound Expression: Or Expression (At least one condition must be true)
class OrExpression extends RegulatoryExpression {
  constructor(expr1, expr2) {
    super();
    this.expr1 = expr1;
    this.expr2 = expr2;
  }

  interpret(context) {
    return this.expr1.interpret(context) || this.expr2.interpret(context);
  }
}

// Context
const drug1Context = {
  clinical_trial_passed: true,
  safety_evaluation_passed: true,
  manufacturing_approved: true
};

const drug2Context = {
  clinical_trial_passed: true,
  safety_evaluation_passed: false,
  manufacturing_approved: true
};

// Create expressions
const clinicalTrialExpr = new ClinicalTrialPassed();
const safetyEvalExpr = new SafetyEvaluationPassed();
const manufacturingExpr = new ManufacturingApproved();

// Create the approval rule expression
const approvalRuleExpr = new AndExpression(
  clinicalTrialExpr,
  new AndExpression(safetyEvalExpr, manufacturingExpr)
);

console.log("Test Small Molecule 01 Approval Status:", approvalRuleExpr.interpret(drug1Context));
console.log("Test Small Molecule 02 Approval Status:", approvalRuleExpr.interpret(drug2Context));

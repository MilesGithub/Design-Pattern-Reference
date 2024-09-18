# Abstract Expression Interface
class RegulatoryExpression:
    def interpret(self, context):
        raise NotImplementedError("This method should be overridden by concrete expressions!")

# Concrete Expression: Clinical Trial Passed
class ClinicalTrialPassed(RegulatoryExpression):
    def interpret(self, context):
        return context.get("clinical_trial_passed", False)

# Concrete Expression: Safety Evaluation Passed
class SafetyEvaluationPassed(RegulatoryExpression):
    def interpret(self, context):
        return context.get("safety_evaluation_passed", False)

# Concrete Expression: Manufacturing Approved
class ManufacturingApproved(RegulatoryExpression):
    def interpret(self, context):
        return context.get("manufacturing_approved", False)

# Compound Expression: And Expression (All conditions must be true)
class AndExpression(RegulatoryExpression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) and self.expr2.interpret(context)

# Compound Expression: Or Expression (At least one condition must be true)
class OrExpression(RegulatoryExpression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) or self.expr2.interpret(context)

# Context
drug1_context = {
    "clinical_trial_passed": True,
    "safety_evaluation_passed": True,
    "manufacturing_approved": True
}

drug2_context = {
    "clinical_trial_passed": True,
    "safety_evaluation_passed": False,
    "manufacturing_approved": True
}

# Create expressions
clinical_trial_expr = ClinicalTrialPassed()
safety_eval_expr = SafetyEvaluationPassed()
manufacturing_expr = ManufacturingApproved()

approval_rule_expr = AndExpression(
    expr1=clinical_trial_expr,
    expr2=AndExpression(
        expr1=safety_eval_expr,
        expr2=manufacturing_expr
    )
)

print("Test Small Molecule 01 Approval Status:", approval_rule_expr.interpret(drug1_context))
print("Test Small Molecule 02 Approval Status:", approval_rule_expr.interpret(drug2_context))

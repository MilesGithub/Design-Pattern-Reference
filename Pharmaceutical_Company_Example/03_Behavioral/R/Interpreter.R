# Abstract Expression Interface
RegulatoryExpression <- setRefClass(
  "RegulatoryExpression",
  methods = list(
    interpret = function(context) {
      stop("This method should be overridden by concrete expressions!")
    }
  )
)

# Concrete Expression: Clinical Trial Passed
ClinicalTrialPassed <- setRefClass(
  "ClinicalTrialPassed",
  contains = "RegulatoryExpression",
  methods = list(
    interpret = function(context) {
      return(context[["clinical_trial_passed"]])
    }
  )
)

# Concrete Expression: Safety Evaluation Passed
SafetyEvaluationPassed <- setRefClass(
  "SafetyEvaluationPassed",
  contains = "RegulatoryExpression",
  methods = list(
    interpret = function(context) {
      return(context[["safety_evaluation_passed"]])
    }
  )
)

# Concrete Expression: Manufacturing Approved
ManufacturingApproved <- setRefClass(
  "ManufacturingApproved",
  contains = "RegulatoryExpression",
  methods = list(
    interpret = function(context) {
      return(context[["manufacturing_approved"]])
    }
  )
)

# Compound Expression: And Expression (All conditions must be true)
AndExpression <- setRefClass(
  "AndExpression",
  contains = "RegulatoryExpression",
  fields = list(expr1 = "ANY", expr2 = "ANY"),
  methods = list(
    interpret = function(context) {
      return(expr1$interpret(context) && expr2$interpret(context))
    }
  )
)

# Compound Expression: Or Expression (At least one condition must be true)
OrExpression <- setRefClass(
  "OrExpression",
  contains = "RegulatoryExpression",
  fields = list(expr1 = "ANY", expr2 = "ANY"),
  methods = list(
    interpret = function(context) {
      return(expr1$interpret(context) || expr2$interpret(context))
    }
  )
)

# Context
drug1_context <- list(clinical_trial_passed = TRUE, safety_evaluation_passed = TRUE, manufacturing_approved = TRUE)
drug2_context <- list(clinical_trial_passed = TRUE, safety_evaluation_passed = FALSE, manufacturing_approved = TRUE)

# Create expressions
clinical_trial_expr <- ClinicalTrialPassed$new()
safety_eval_expr <- SafetyEvaluationPassed$new()
manufacturing_expr <- ManufacturingApproved$new()

approval_rule_expr <- AndExpression$new(expr1 = clinical_trial_expr, expr2 = AndExpression$new(expr1 = safety_eval_expr, expr2 = manufacturing_expr))

message("Test Small Molecule 01", "Approval Status:", approval_rule_expr$interpret(drug1_context))
message("Test Small Molecule 02", "Approval Status:", approval_rule_expr$interpret(drug2_context))

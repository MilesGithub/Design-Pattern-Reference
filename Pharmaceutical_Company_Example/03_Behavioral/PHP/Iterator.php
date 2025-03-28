<?php

// Abstract Expression Interface
abstract class RegulatoryExpression {
    abstract public function interpret($context);
}

// Concrete Expression: Clinical Trial Passed
class ClinicalTrialPassed extends RegulatoryExpression {
    public function interpret($context) {
        return isset($context['clinical_trial_passed']) ? $context['clinical_trial_passed'] : false;
    }
}

// Concrete Expression: Safety Evaluation Passed
class SafetyEvaluationPassed extends RegulatoryExpression {
    public function interpret($context) {
        return isset($context['safety_evaluation_passed']) ? $context['safety_evaluation_passed'] : false;
    }
}

// Concrete Expression: Manufacturing Approved
class ManufacturingApproved extends RegulatoryExpression {
    public function interpret($context) {
        return isset($context['manufacturing_approved']) ? $context['manufacturing_approved'] : false;
    }
}

// Compound Expression: And Expression (All conditions must be true)
class AndExpression extends RegulatoryExpression {
    private $expr1;
    private $expr2;

    public function __construct($expr1, $expr2) {
        $this->expr1 = $expr1;
        $this->expr2 = $expr2;
    }

    public function interpret($context) {
        return $this->expr1->interpret($context) && $this->expr2->interpret($context);
    }
}

// Compound Expression: Or Expression (At least one condition must be true)
class OrExpression extends RegulatoryExpression {
    private $expr1;
    private $expr2;

    public function __construct($expr1, $expr2) {
        $this->expr1 = $expr1;
        $this->expr2 = $expr2;
    }

    public function interpret($context) {
        return $this->expr1->interpret($context) || $this->expr2->interpret($context);
    }
}

// Context
$drug1_context = [
    "clinical_trial_passed" => true,
    "safety_evaluation_passed" => true,
    "manufacturing_approved" => true
];

$drug2_context = [
    "clinical_trial_passed" => true,
    "safety_evaluation_passed" => false,
    "manufacturing_approved" => true
];

// Create expressions
$clinical_trial_expr = new ClinicalTrialPassed();
$safety_eval_expr = new SafetyEvaluationPassed();
$manufacturing_expr = new ManufacturingApproved();

$approval_rule_expr = new AndExpression(
    $clinical_trial_expr,
    new AndExpression(
        $safety_eval_expr,
        $manufacturing_expr
    )
);

echo "Test Small Molecule 01 Approval Status: " . ($approval_rule_expr->interpret($drug1_context) ? "Approved" : "Not Approved") . "\n";
echo "Test Small Molecule 02 Approval Status: " . ($approval_rule_expr->interpret($drug2_context) ? "Approved" : "Not Approved") . "\n";

?>

// Abstract Expression Interface
interface RegulatoryExpression {
    boolean interpret(java.util.Map<String, Boolean> context);
}

// Concrete Expression: Clinical Trial Passed
class ClinicalTrialPassed implements RegulatoryExpression {
    @Override
    public boolean interpret(java.util.Map<String, Boolean> context) {
        return context.getOrDefault("clinical_trial_passed", false);
    }
}

// Concrete Expression: Safety Evaluation Passed
class SafetyEvaluationPassed implements RegulatoryExpression {
    @Override
    public boolean interpret(java.util.Map<String, Boolean> context) {
        return context.getOrDefault("safety_evaluation_passed", false);
    }
}

// Concrete Expression: Manufacturing Approved
class ManufacturingApproved implements RegulatoryExpression {
    @Override
    public boolean interpret(java.util.Map<String, Boolean> context) {
        return context.getOrDefault("manufacturing_approved", false);
    }
}

// Compound Expression: And Expression (All conditions must be true)
class AndExpression implements RegulatoryExpression {
    private RegulatoryExpression expr1;
    private RegulatoryExpression expr2;

    public AndExpression(RegulatoryExpression expr1, RegulatoryExpression expr2) {
        this.expr1 = expr1;
        this.expr2 = expr2;
    }

    @Override
    public boolean interpret(java.util.Map<String, Boolean> context) {
        return expr1.interpret(context) && expr2.interpret(context);
    }
}

// Compound Expression: Or Expression (At least one condition must be true)
class OrExpression implements RegulatoryExpression {
    private RegulatoryExpression expr1;
    private RegulatoryExpression expr2;

    public OrExpression(RegulatoryExpression expr1, RegulatoryExpression expr2) {
        this.expr1 = expr1;
        this.expr2 = expr2;
    }

    @Override
    public boolean interpret(java.util.Map<String, Boolean> context) {
        return expr1.interpret(context) || expr2.interpret(context);
    }
}

public class Main {
    public static void main(String[] args) {
        // Context for drug approval
        java.util.Map<String, Boolean> drug1Context = new java.util.HashMap<>();
        drug1Context.put("clinical_trial_passed", true);
        drug1Context.put("safety_evaluation_passed", true);
        drug1Context.put("manufacturing_approved", true);

        java.util.Map<String, Boolean> drug2Context = new java.util.HashMap<>();
        drug2Context.put("clinical_trial_passed", true);
        drug2Context.put("safety_evaluation_passed", false);
        drug2Context.put("manufacturing_approved", true);

        // Create expressions
        RegulatoryExpression clinicalTrialExpr = new ClinicalTrialPassed();
        RegulatoryExpression safetyEvalExpr = new SafetyEvaluationPassed();
        RegulatoryExpression manufacturingExpr = new ManufacturingApproved();

        RegulatoryExpression approvalRuleExpr = new AndExpression(
            clinicalTrialExpr,
            new AndExpression(safetyEvalExpr, manufacturingExpr)
        );

        // Evaluate the approval status
        System.out.println("Test Small Molecule 01 Approval Status: " + approvalRuleExpr.interpret(drug1Context));
        System.out.println("Test Small Molecule 02 Approval Status: " + approvalRuleExpr.interpret(drug2Context));
    }
}

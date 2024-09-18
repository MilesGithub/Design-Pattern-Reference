# Component
class RegulatoryProcess:
    def execute(self):
        raise NotImplementedError("This method should be implemented by subclasses.")


# Leaf
class Step(RegulatoryProcess):
    def __init__(self, step_name):
        self.step_name = step_name

    def execute(self):
        print(f"Executing step: {self.step_name}")


# Composite
class CompositeProcess(RegulatoryProcess):
    def __init__(self, process_name):
        self.process_name = process_name
        self.children = []

    def add(self, regulatory_process):
        self.children.append(regulatory_process)

    def remove(self, regulatory_process):
        self.children.remove(regulatory_process)

    def execute(self):
        print(f"Executing composite process: {self.process_name}")
        for child in self.children:
            child.execute()


# Leaf objects - individual steps
clinical_trial_step = Step("Clinical Trial Approval")
safety_step = Step("Safety Review")
manufacturing_step = Step("Manufacturing Validation")

# Composite processes
clinical_process = CompositeProcess("Clinical Process")
clinical_process.add(clinical_trial_step)

regulatory_process = CompositeProcess("Regulatory Process")
regulatory_process.add(safety_step)
regulatory_process.add(manufacturing_step)

full_approval_process = CompositeProcess("Full Drug Approval Process")
full_approval_process.add(clinical_process)
full_approval_process.add(regulatory_process)

full_approval_process.execute()

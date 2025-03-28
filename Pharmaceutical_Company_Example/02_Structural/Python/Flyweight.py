# Flyweight class
class RegulatoryProcessFlyweight:
    def __init__(self):
        self.common_regulatory_steps = [
            "Submit Trial Data",
            "Review Trial Data",
            "Submit Safety Data",
            "Review Safety Data",
            "Submit Regulatory Documents",
            "Obtain Regulatory Approval"
        ]
    
    def get_steps(self):
        return self.common_regulatory_steps

# Flyweight Factory
class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}
    
    def get_flyweight(self, key):
        if key not in self.flyweights:
            print(f"Creating new flyweight for: {key}")
            flyweight = RegulatoryProcessFlyweight()
            self.flyweights[key] = flyweight
        else:
            print(f"Reusing existing flyweight for: {key}")
        return self.flyweights[key]

# Uses flyweights for shared regulatory processes
class Drug:
    def __init__(self, name, flyweight):
        self.name = name
        self.flyweight = flyweight
        self.regulatory_steps = flyweight.get_steps()
    
    def display_regulatory_process(self):
        print(f"Regulatory process for {self.name}:")
        for step in self.regulatory_steps:
            print(f" - {step}")


flyweight_factory = FlyweightFactory()

drug1 = Drug("Test Small Molecule 01", flyweight_factory.get_flyweight("Standard Process"))
drug2 = Drug("Test Small Molecule 02", flyweight_factory.get_flyweight("Standard Process"))
drug3 = Drug("Test Monoclonal Antibody 01", flyweight_factory.get_flyweight("Standard Process"))

drug1.display_regulatory_process()
drug2.display_regulatory_process()
drug3.display_regulatory_process()

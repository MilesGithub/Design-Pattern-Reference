# Abstraction
class RegulatoryProcess:
    def __init__(self, implementation):
        self.implementation = implementation

    def submit(self):
        self.implementation.submit()

    def approve(self):
        self.implementation.approve()


# Concrete implementation for Vaccines
class VaccineProcess:
    def submit(self):
        print("Submitting vaccine clinical trial data...")

    def approve(self):
        print("Vaccine regulatory approval granted.")


# Concrete implementation for Small-Molecule Drugs
class SmallMoleculeDrugProcess:
    def submit(self):
        print("Submitting small-molecule clinical trial data...")

    def approve(self):
        print("Small-molecule regulatory approval granted.")


# Concrete implementation for Biologics
class BiologicsProcess:
    def submit(self):
        print("Submitting biologics clinical trial data...")

    def approve(self):
        print("Biologics regulatory approval granted.")


preclinical_small_molecule = RegulatoryProcess(SmallMoleculeDrugProcess())
preclinical_small_molecule.submit()
preclinical_small_molecule.approve()

clinical_biologics = RegulatoryProcess(SmallMoleculeDrugProcess())
clinical_biologics.submit()
clinical_biologics.approve()

clinical_vaccine = RegulatoryProcess(VaccineProcess())
clinical_vaccine.submit()
clinical_vaccine.approve()

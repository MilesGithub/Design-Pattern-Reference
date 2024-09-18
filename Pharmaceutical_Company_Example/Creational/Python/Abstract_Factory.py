from abc import ABC, abstractmethod

# Abstract Factory Interface
class RegulatoryFactory(ABC):
    @abstractmethod
    def create_submission_form(self):
        pass

    @abstractmethod
    def create_testing_protocol(self):
        pass

# Concrete Factory for Vaccines
class VaccineRegulatoryFactory(RegulatoryFactory):
    def create_submission_form(self):
        return VaccineSubmissionForm()

    def create_testing_protocol(self):
        return VaccineTestingProtocol()

# Concrete Factory for Small-Molecule Drugs
class SmallMoleculeRegulatoryFactory(RegulatoryFactory):
    def create_submission_form(self):
        return SmallMoleculeSubmissionForm()

    def create_testing_protocol(self):
        return SmallMoleculeTestingProtocol()

# Concrete Factory for Biologics
class BiologicsRegulatoryFactory(RegulatoryFactory):
    def create_submission_form(self):
        return BiologicsSubmissionForm()

    def create_testing_protocol(self):
        return BiologicsTestingProtocol()

# Abstract Product
class SubmissionForm(ABC):
    @abstractmethod
    def submit(self):
        pass

# Concrete Product: Vaccine Submission Form
class VaccineSubmissionForm(SubmissionForm):
    def submit(self):
        print("Submitting vaccine clinical trial data form.")

# Concrete Product: Small-Molecule Submission Form
class SmallMoleculeSubmissionForm(SubmissionForm):
    def submit(self):
        print("Submitting small-molecule drug trial data form.")

# Concrete Product: Biologics Submission Form
class BiologicsSubmissionForm(SubmissionForm):
    def submit(self):
        print("Submitting biologics clinical trial data form.")

# Abstract Product
class TestingProtocol(ABC):
    @abstractmethod
    def run_tests(self):
        pass

# Concrete Product: Vaccine Testing Protocol
class VaccineTestingProtocol(TestingProtocol):
    def run_tests(self):
        print("Running tests for vaccines.")

# Concrete Product: Small-Molecule Testing Protocol
class SmallMoleculeTestingProtocol(TestingProtocol):
    def run_tests(self):
        print("Running tests for small-molecule drugs.")

# Concrete Product: Biologics Testing Protocol
class BiologicsTestingProtocol(TestingProtocol):
    def run_tests(self):
        print("Running tests for biologics.")


def process_regulatory_approval(factory: RegulatoryFactory):
    submission_form = factory.create_submission_form()
    testing_protocol = factory.create_testing_protocol()
    
    submission_form.submit()
    testing_protocol.run_tests()

# Vaccine Regulatory Process
vaccine_factory = VaccineRegulatoryFactory()
process_regulatory_approval(vaccine_factory)

# Small-Molecule Drug Regulatory Process
small_molecule_factory = SmallMoleculeRegulatoryFactory()
process_regulatory_approval(small_molecule_factory)

# Biologics Regulatory Process
biologics_factory = BiologicsRegulatoryFactory()
process_regulatory_approval(biologics_factory)

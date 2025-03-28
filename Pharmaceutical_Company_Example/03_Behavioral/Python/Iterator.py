from typing import List, Dict, Optional

# Iterator Interface
class ApplicationIterator:
    def has_next(self) -> bool:
        raise NotImplementedError("This method should be overridden!")

    def is_next(self) -> Optional[Dict[str, str]]:
        raise NotImplementedError("This method should be overridden!")

# Concrete Iterator
class DrugApplicationIterator(ApplicationIterator):
    def __init__(self, applications: List[Dict[str, str]]):
        self.applications = applications
        self.position = 0

    def has_next(self) -> bool:
        return self.position < len(self.applications)

    def is_next(self) -> Optional[Dict[str, str]]:
        if self.has_next():
            app = self.applications[self.position]
            self.position += 1
            return app
        return None

# Aggregate Interface
class ApplicationCollection:
    def create_iterator(self) -> ApplicationIterator:
        raise NotImplementedError("This method should be overridden!")

# Concrete Aggregate
class DrugApplicationCollection(ApplicationCollection):
    def __init__(self):
        self.applications = []

    def add_application(self, application: Dict[str, str]):
        self.applications.append(application)

    def create_iterator(self) -> DrugApplicationIterator:
        return DrugApplicationIterator(self.applications)


drug_collection = DrugApplicationCollection()

drug_collection.add_application({"drug_name": "Test Vaccine 01", "status": "Under Review"})
drug_collection.add_application({"drug_name": "Test Small Molecule 01", "status": "Approved"})
drug_collection.add_application({"drug_name": "Test Monoclonal Antibody 01", "status": "Rejected"})

iterator = drug_collection.create_iterator()

# Use the iterator to traverse the applications
while iterator.has_next():
    application = iterator.is_next()
    if application:
        print(f"Drug Name: {application['drug_name']} - Status: {application['status']}")

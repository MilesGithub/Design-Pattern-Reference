// Iterator Interface
class ApplicationIterator {
  hasNext() {
    throw new Error("This method should be overridden!");
  }

  isNext() {
    throw new Error("This method should be overridden!");
  }
}

// Concrete Iterator
class DrugApplicationIterator extends ApplicationIterator {
  constructor(applications) {
    super();
    this.applications = applications;
    this.position = 0;
  }

  hasNext() {
    return this.position < this.applications.length;
  }

  isNext() {
    if (this.hasNext()) {
      const app = this.applications[this.position];
      this.position += 1;
      return app;
    }
    return null;
  }
}

// Aggregate Interface
class ApplicationCollection {
  createIterator() {
    throw new Error("This method should be overridden!");
  }
}

// Concrete Aggregate
class DrugApplicationCollection extends ApplicationCollection {
  constructor() {
    super();
    this.applications = [];
  }

  addApplication(application) {
    this.applications.push(application);
  }

  createIterator() {
    return new DrugApplicationIterator(this.applications);
  }
}

const drugCollection = new DrugApplicationCollection();

drugCollection.addApplication({ drug_name: "Test Vaccine 01", status: "Under Review" });
drugCollection.addApplication({ drug_name: "Test Small Molecule 01", status: "Approved" });
drugCollection.addApplication({ drug_name: "Test Monoclonal Antibody 01", status: "Rejected" });

const iterator = drugCollection.createIterator();

// Use the iterator to traverse the applications
while (iterator.hasNext()) {
  const application = iterator.isNext();
  if (application) {
    console.log(`Drug Name: ${application.drug_name} - Status: ${application.status}`);
  }
}

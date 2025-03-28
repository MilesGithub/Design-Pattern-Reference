#include <iostream>
#include <vector>
#include <memory>
#include <string>
#include <unordered_map>

using namespace std;

// Iterator Interface
class ApplicationIterator {
public:
  virtual bool hasNext() const = 0;
  virtual shared_ptr<unordered_map<string, string>> next() = 0;
  virtual ~ApplicationIterator() = default;
};

// Concrete Iterator
class DrugApplicationIterator : public ApplicationIterator {
private:
  vector<shared_ptr<unordered_map<string, string>>> applications;
  size_t position = 0;
  
public:
  DrugApplicationIterator(const vector<shared_ptr<unordered_map<string, string>>>& apps)
    : applications(apps) {}
  
  bool hasNext() const override {
    return position < applications.size();
  }
  
  shared_ptr<unordered_map<string, string>> next() override {
    if (hasNext()) {
      return applications[position++];
    }
    return nullptr;
  }
};

// Aggregate Interface
class ApplicationCollection {
public:
  virtual shared_ptr<ApplicationIterator> createIterator() = 0;
  virtual ~ApplicationCollection() = default;
};

// Concrete Aggregate
class DrugApplicationCollection : public ApplicationCollection {
private:
  vector<shared_ptr<unordered_map<string, string>>> applications;
  
public:
  void addApplication(const unordered_map<string, string>& application) {
    applications.push_back(make_shared<unordered_map<string, string>>(application));
  }
  
  shared_ptr<ApplicationIterator> createIterator() override {
    return make_shared<DrugApplicationIterator>(applications);
  }
};

int main() {
  DrugApplicationCollection drugCollection;
  
  // Adding applications
  drugCollection.addApplication({{"drug_name", "Test Vaccine 01"}, {"status", "Under Review"}});
  drugCollection.addApplication({{"drug_name", "Test Small Molecule 01"}, {"status", "Approved"}});
  drugCollection.addApplication({{"drug_name", "Test Monoclonal Antibody 01"}, {"status", "Rejected"}});
  
  // Create iterator
  auto iterator = drugCollection.createIterator();
  
  // Use the iterator to traverse the applications
  while (iterator->hasNext()) {
    auto application = iterator->next();
    if (application) {
      cout << "Drug Name: " << (*application)["drug_name"] << " - Status: " << (*application)["status"] << endl;
    }
  }
  
  return 0;
}

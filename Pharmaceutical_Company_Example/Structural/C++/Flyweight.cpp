#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

// Flyweight class
class RegulatoryProcessFlyweight {
public:
  RegulatoryProcessFlyweight() {
    commonRegulatorySteps = {
      "Submit Trial Data", 
      "Review Trial Data", 
      "Submit Safety Data", 
      "Review Safety Data", 
      "Submit Regulatory Documents", 
      "Obtain Regulatory Approval"
    };
  }
  
  const std::vector<std::string>& getSteps() const {
    return commonRegulatorySteps;
  }
  
private:
  std::vector<std::string> commonRegulatorySteps;
};

// Flyweight Factory
class FlyweightFactory {
public:
  FlyweightFactory() {}
  
  RegulatoryProcessFlyweight* getFlyweight(const std::string& key) {
    if (flyweights.find(key) == flyweights.end()) {
      std::cout << "Creating new flyweight for: " << key << std::endl;
      flyweights[key] = new RegulatoryProcessFlyweight();
    } else {
      std::cout << "Reusing existing flyweight for: " << key << std::endl;
    }
    return flyweights[key];
  }
  
  ~FlyweightFactory() {
    // Clean up dynamically allocated flyweights
    for (auto& pair : flyweights) {
      delete pair.second;
    }
  }
  
private:
  std::unordered_map<std::string, RegulatoryProcessFlyweight*> flyweights;
};

// Uses flyweights for shared regulatory processes
class Drug {
public:
  Drug(const std::string& name, RegulatoryProcessFlyweight* flyweight) 
    : name(name), flyweight(flyweight) {
    regulatorySteps = flyweight->getSteps();
  }
  
  void displayRegulatoryProcess() const {
    std::cout << "Regulatory process for " << name << ":\n";
    for (const auto& step : regulatorySteps) {
      std::cout << " - " << step << std::endl;
    }
  }
  
private:
  std::string name;
  RegulatoryProcessFlyweight* flyweight;
  const std::vector<std::string>& regulatorySteps;
};

int main() {
  FlyweightFactory flyweightFactory;
  
  Drug drug1("Test Small Molecule 01", flyweightFactory.getFlyweight("Standard Process"));
  Drug drug2("Test Small Molecule 02", flyweightFactory.getFlyweight("Standard Process"));
  Drug drug3("Test Monoclonal Antibody 01", flyweightFactory.getFlyweight("Standard Process"));
  
  drug1.displayRegulatoryProcess();
  drug2.displayRegulatoryProcess();
  drug3.displayRegulatoryProcess();
  
  return 0;
}

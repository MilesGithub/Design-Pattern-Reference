#include <iostream>
#include <vector>
#include <string>
#include <memory>

using namespace std;

// Memento
class DrugApplicationMemento {
private:
  string _state;
  
public:
  explicit DrugApplicationMemento(const string& state) : _state(state) {}
  
  string getState() const {
    return _state;
  }
};

// Originator
class DrugApplication {
private:
  string _state;
  
public:
  void setState(const string& newState) {
    _state = newState;
    cout << "DrugApplication: State has changed to: " << _state << endl;
  }
  
  shared_ptr<DrugApplicationMemento> createMemento() const {
    return make_shared<DrugApplicationMemento>(_state);
  }
  
  void restoreMemento(const shared_ptr<DrugApplicationMemento>& memento) {
    _state = memento->getState();
    cout << "DrugApplication: State restored to: " << _state << endl;
  }
};

// Caretaker
class ApplicationCaretaker {
private:
  vector<shared_ptr<DrugApplicationMemento>> _mementos;
  
public:
  void saveMemento(const shared_ptr<DrugApplicationMemento>& memento) {
    _mementos.push_back(memento);
    cout << "ApplicationCaretaker: Saved state." << endl;
  }
  
  shared_ptr<DrugApplicationMemento> getMemento(int index) const {
    if (index >= 0 && index < _mementos.size()) {
      return _mementos[index];
    } else {
      throw out_of_range("Invalid index for memento retrieval.");
    }
  }
};

int main() {
  // Create DrugApplication and ApplicationCaretaker instances
  DrugApplication drugApplication;
  ApplicationCaretaker caretaker;
  
  // Set initial state
  drugApplication.setState("Submitted");
  caretaker.saveMemento(drugApplication.createMemento());
  
  // Change state to clinical trial and save
  drugApplication.setState("Clinical Trial");
  caretaker.saveMemento(drugApplication.createMemento());
  
  // Change state to review and save
  drugApplication.setState("Under Review");
  caretaker.saveMemento(drugApplication.createMemento());
  
  // Change state to approved
  drugApplication.setState("Approved");
  
  // Restore to previous state: Under Review
  drugApplication.restoreMemento(caretaker.getMemento(2));
  
  // Restore to an earlier state: Clinical Trial
  drugApplication.restoreMemento(caretaker.getMemento(1));
  
  // Restore to the initial state: Submitted
  drugApplication.restoreMemento(caretaker.getMemento(0));
  
  return 0;
}

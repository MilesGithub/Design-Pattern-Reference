# Memento
DrugApplicationMemento <- setRefClass(
  "DrugApplicationMemento",
  fields = list(state = "character"),
  methods = list(
    get_state = function() {
      return(state)
    }
  )
)

# Originator
DrugApplication <- setRefClass(
  "DrugApplication",
  fields = list(state = "character"),
  methods = list(
    set_state = function(new_state) {
      state <<- new_state
      message("DrugApplication: State has changed to:", state)
    },
    create_memento = function() {
      return(DrugApplicationMemento$new(state = state))
    },
    restore_memento = function(memento) {
      state <<- memento$get_state()
      message("DrugApplication: State restored to:", state)
    }
  )
)

# Caretaker
ApplicationCaretaker <- setRefClass(
  "ApplicationCaretaker",
  fields = list(mementos = "list"),
  methods = list(
    save_memento = function(memento) {
      mementos[[length(mementos) + 1]] <<- memento
      message("ApplicationCaretaker: Saved state.\n")
    },
    get_memento = function(index) {
      if (index > 0 && index <= length(mementos)) {
        return(mementos[[index]])
      } else {
        stop("Invalid index for memento retrieval.")
      }
    }
  )
)

drug_application <- DrugApplication$new()

# Create caretaker to save and restore states
caretaker <- ApplicationCaretaker$new()

# Set initial state
drug_application$set_state("Submitted")
caretaker$save_memento(drug_application$create_memento())

# Change state to clinical trial and save
drug_application$set_state("Clinical Trial")
caretaker$save_memento(drug_application$create_memento())

# Change state to review and save
drug_application$set_state("Under Review")
caretaker$save_memento(drug_application$create_memento())

# Change state to approved
drug_application$set_state("Approved")


# Restore to previous state: Under Review
drug_application$restore_memento(caretaker$get_memento(3))

# Restore to an earlier state: Clinical Trial
drug_application$restore_memento(caretaker$get_memento(2))

# Restore to the initial state: Submitted
drug_application$restore_memento(caretaker$get_memento(1))

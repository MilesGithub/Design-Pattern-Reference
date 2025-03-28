# State interface
DrugState <- setRefClass(
  "DrugState",
  methods = list(
    proceed_to_next = function() {
      stop("This method should be overridden by concrete states!")
    },
    get_state_name = function() {
      stop("This method should be overridden by concrete states!")
    }
  )
)

# Submitted State
SubmittedState <- setRefClass(
  "SubmittedState",
  contains = "DrugState",
  methods = list(
    proceed_to_next = function(drug_application) {
      message("Proceeding from Submitted to Clinical Trial...")
      drug_application$set_state(ClinicalTrialState$new())
    },
    get_state_name = function() {
      return("Submitted")
    }
  )
)

# Clinical Trial State
ClinicalTrialState <- setRefClass(
  "ClinicalTrialState",
  contains = "DrugState",
  methods = list(
    proceed_to_next = function(drug_application) {
      message("Proceeding from Clinical Trial to Under Review...")
      drug_application$set_state(UnderReviewState$new())
    },
    get_state_name = function() {
      return("Clinical Trial")
    }
  )
)

# Under Review State
UnderReviewState <- setRefClass(
  "UnderReviewState",
  contains = "DrugState",
  methods = list(
    proceed_to_next = function(drug_application) {
      message("Proceeding from Under Review to Approved...")
      drug_application$set_state(ApprovedState$new())
    },
    get_state_name = function() {
      return("Under Review")
    }
  )
)

# Approved State
ApprovedState <- setRefClass(
  "ApprovedState",
  contains = "DrugState",
  methods = list(
    proceed_to_next = function(drug_application) {
      message("The drug has already been approved. No further states.")
    },
    get_state_name = function() {
      return("Approved")
    }
  )
)

# Context class
DrugApplication <- setRefClass(
  "DrugApplication",
  fields = list(state = "DrugState"),
  methods = list(
    set_state = function(new_state) {
      state <<- new_state
      message("DrugApplication: State changed to:", state$get_state_name())
    },
    proceed = function() {
      state$proceed_to_next(.self)
    },
    get_current_state = function() {
      return(state$get_state_name())
    }
  )
)

# Initial drug application in "Submitted" state
drug_application <- DrugApplication$new(state = SubmittedState$new())

drug_application$proceed()  # Moves to Clinical Trial
drug_application$proceed()  # Moves to Under Review
drug_application$proceed()  # Moves to Approved
drug_application$proceed()  # Already Approved, no further state

# Observer Interface
Observer <- setRefClass(
  "Observer",
  methods = list(
    update = function(state) {
      stop("This method should be overridden by concrete observers!")
    }
  )
)

# Subject
DrugApprovalProcess <- setRefClass(
  "DrugApprovalProcess",
  fields = list(observers = "list", state = "character"),
  methods = list(
    attach_observer = function(observer) {
      observers[[length(observers) + 1]] <<- observer
    },
    detach_observer = function(observer) {
      observers <<- observers[!sapply(observers, identical, observer)]
    },
    notify_observers = function() {
      message("DrugApprovalProcess: Notifying observers about state change to:", state)
      for (observer in observers) {
        observer$update(state)
      }
    },
    set_state = function(new_state) {
      state <<- new_state
      message("DrugApprovalProcess: State changed to:", state)
      notify_observers()
    }
  )
)

# Clinical Trials Department
ClinicalTrials <- setRefClass(
  "ClinicalTrials",
  contains = "Observer",
  methods = list(
    update = function(state) {
      message("Clinical Trials Department: Notified about state change to:", state)
    }
  )
)

# Quality Assurance Department
QualityAssurance <- setRefClass(
  "QualityAssurance",
  contains = "Observer",
  methods = list(
    update = function(state) {
      message("Quality Assurance Department: Notified about state change to:", state)
    }
  )
)

# Legal Department
LegalDepartment <- setRefClass(
  "LegalDepartment",
  contains = "Observer",
  methods = list(
    update = function(state) {
      message("Legal Department: Notified about state change to:", state)
    }
  )
)

# Regulatory Affairs Department
RegulatoryAffairs <- setRefClass(
  "RegulatoryAffairs",
  contains = "Observer",
  methods = list(
    update = function(state) {
      message("Regulatory Affairs Department: Notified about state change to:", state)
    }
  )
)

drug_approval_process <- DrugApprovalProcess$new()

# Create observers
clinical_trials <- ClinicalTrials$new()
quality_assurance <- QualityAssurance$new()
legal <- LegalDepartment$new()
regulatory_affairs <- RegulatoryAffairs$new()

# Attach observers to the subject
drug_approval_process$attach_observer(clinical_trials)
drug_approval_process$attach_observer(quality_assurance)
drug_approval_process$attach_observer(legal)
drug_approval_process$attach_observer(regulatory_affairs)

# Simulate state changes and notify observers
drug_approval_process$set_state("Clinical Trial Started")
drug_approval_process$set_state("Clinical Trial Completed")
drug_approval_process$set_state("Quality Check in Progress")
drug_approval_process$set_state("Under Regulatory Review")
drug_approval_process$set_state("Approved")

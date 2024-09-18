# Mediator Interface
Mediator <- setRefClass(
  "Mediator",
  methods = list(
    notify = function(sender, event) {
      stop("This method should be overridden by concrete mediators!")
    }
  )
)

# Concrete Mediator
RegulatoryMediator <- setRefClass(
  "RegulatoryMediator",
  contains = "Mediator",  # <-- Explicit inheritance from Mediator
  fields = list(clinical_trials = "ANY", quality_assurance = "ANY", regulatory_affairs = "ANY", legal = "ANY"),
  methods = list(
    notify = function(sender, event) {
      if (event == "Clinical Trial Completed") {
        message("Mediator: Clinical Trial completed. Notifying Quality Assurance.")
        quality_assurance$check_quality()
      } else if (event == "Quality Check Completed") {
        message("Mediator: Quality Check completed. Notifying Regulatory Affairs.")
        regulatory_affairs$prepare_documents()
      } else if (event == "Documents Prepared") {
        message("Mediator: Documents prepared. Notifying Legal Department.")
        legal$review_documents()
      } else if (event == "Legal Review Completed") {
        message("Mediator: Legal Review completed. Drug is ready for final approval.")
      }
    }
  )
)

# Department Interfaces
Department <- setRefClass(
  "Department",
  fields = list(mediator = "Mediator"),
  methods = list(
    complete_task = function() {
      stop("This method should be overridden by concrete departments!")
    }
  )
)

# Concrete Department: Clinical Trials
ClinicalTrials <- setRefClass(
  "ClinicalTrials",
  contains = "Department",
  methods = list(
    run_trials = function() {
      message("Clinical Trials: Running clinical trials...")
      mediator$notify(.self, "Clinical Trial Completed")
    }
  )
)

# Concrete Department: Quality Assurance
QualityAssurance <- setRefClass(
  "QualityAssurance",
  contains = "Department",
  methods = list(
    check_quality = function() {
      message("Quality Assurance: Checking product quality...")
      mediator$notify(.self, "Quality Check Completed")
    }
  )
)

# Concrete Department: Regulatory Affairs
RegulatoryAffairs <- setRefClass(
  "RegulatoryAffairs",
  contains = "Department",
  methods = list(
    prepare_documents = function() {
      message("Regulatory Affairs: Preparing regulatory documents...")
      mediator$notify(.self, "Documents Prepared")
    }
  )
)

# Concrete Department: Legal Department
LegalDepartment <- setRefClass(
  "LegalDepartment",
  contains = "Department",
  methods = list(
    review_documents = function() {
      message("Legal Department: Reviewing regulatory documents...")
      mediator$notify(.self, "Legal Review Completed")
    }
  )
)

# Create the Mediator
mediator <- RegulatoryMediator$new()

# Create Departments
clinical_trials <- ClinicalTrials$new(mediator = mediator)
quality_assurance <- QualityAssurance$new(mediator = mediator)
regulatory_affairs <- RegulatoryAffairs$new(mediator = mediator)
legal <- LegalDepartment$new(mediator = mediator)

# Set Departments in the Mediator
mediator$clinical_trials <- clinical_trials
mediator$quality_assurance <- quality_assurance
mediator$regulatory_affairs <- regulatory_affairs
mediator$legal <- legal

# Run process
clinical_trials$run_trials()

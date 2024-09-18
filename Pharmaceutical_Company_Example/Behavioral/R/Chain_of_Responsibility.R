
# Base class for a drug approval request handler
DrugApprovalHandler <- setRefClass(
  "DrugApprovalHandler",
  fields = list(next_handler = "ANY"),
  methods = list(
    set_next = function(handler) {
      .self$next_handler <- handler
      return(handler)
    },
    handle_request = function(drug) {
      stop("This method should be implemented by subclasses.")
    },
    pass_to_next = function(drug) {
      if (!is.null(.self$next_handler)) {
        .self$next_handler$handle_request(drug)
      } else {
        message("End of chain, no handler could process the request.")
      }
    }
  )
)

# Concrete handler for Initial Review
InitialReviewHandler <- setRefClass(
  "InitialReviewHandler",
  contains = "DrugApprovalHandler",
  methods = list(
    handle_request = function(drug) {
      if (drug$initial_review_status == "Pending") {
        message("Initial review passed for ", drug$name)
        drug$initial_review_status <- "Approved"
        .self$pass_to_next(drug)
      } else {
        message("Initial review already processed for ", drug$name)
        .self$pass_to_next(drug)
      }
    }
  )
)

# Concrete handler for Clinical Trials Review
ClinicalTrialsHandler <- setRefClass(
  "ClinicalTrialsHandler",
  contains = "DrugApprovalHandler",
  methods = list(
    handle_request = function(drug) {
      if (drug$clinical_trials_status == "Pending") {
        message("Clinical trials review passed for ", drug$name)
        drug$clinical_trials_status <- "Approved"
        .self$pass_to_next(drug)
      } else {
        message("Clinical trials already processed for ", drug$name)
        .self$pass_to_next(drug)
      }
    }
  )
)

# Concrete handler for Regulatory Review
RegulatoryReviewHandler <- setRefClass(
  "RegulatoryReviewHandler",
  contains = "DrugApprovalHandler",
  methods = list(
    handle_request = function(drug) {
      if (drug$regulatory_status == "Pending") {
        message("Regulatory review passed for ", drug$name)
        drug$regulatory_status <- "Approved"
        .self$pass_to_next(drug)
      } else {
        message("Regulatory review already processed for ", drug$name)
        .self$pass_to_next(drug)
      }
    }
  )
)

# Concrete handler for Final Approval
FinalApprovalHandler <- setRefClass(
  "FinalApprovalHandler",
  contains = "DrugApprovalHandler",
  methods = list(
    handle_request = function(drug) {
      if (drug$initial_review_status == "Approved" &&
          drug$clinical_trials_status == "Approved" &&
          drug$regulatory_status == "Approved") {
        message("Final approval granted for ", drug$name)
        drug$final_approval_status <- "Approved"
      } else {
        message("Drug ", drug$name, " could not pass final approval.")
      }
    }
  )
)

# Drug object
Drug <- setRefClass(
  "Drug",
  fields = list(
    name = "character",
    initial_review_status = "character",
    clinical_trials_status = "character",
    regulatory_status = "character",
    final_approval_status = "character"
  )
)

# Setup the chain of responsibility
initial_review <- InitialReviewHandler$new()
clinical_trials <- ClinicalTrialsHandler$new()
regulatory_review <- RegulatoryReviewHandler$new()
final_approval <- FinalApprovalHandler$new()

initial_review$set_next(clinical_trials)$set_next(regulatory_review)$set_next(final_approval)

drug1 <- Drug$new(
  name = "Test Small Molecule 01",
  initial_review_status = "Pending",
  clinical_trials_status = "Pending",
  regulatory_status = "Pending",
  final_approval_status = "Pending"
)

initial_review$handle_request(drug1)

# Define the Strategy Interface
RegulatoryStrategy <- setRefClass(
  "RegulatoryStrategy",
  methods = list(
    approve_application = function(drug_name) {
      stop("This method should be overridden by concrete strategies!")
    }
  )
)

# Concrete Strategy: Standard Approval
StandardApprovalStrategy <- setRefClass(
  "StandardApprovalStrategy",
  contains = "RegulatoryStrategy",
  methods = list(
    approve_application = function(drug_name) {
      message("Applying Standard Approval Process for drug:", drug_name)
      message(drug_name, "has been approved using the Standard Approval Strategy.")
    }
  )
)

# Concrete Strategy: Accelerated Approval
AcceleratedApprovalStrategy <- setRefClass(
  "AcceleratedApprovalStrategy",
  contains = "RegulatoryStrategy",
  methods = list(
    approve_application = function(drug_name) {
      message("Applying Accelerated Approval Process for drug:", drug_name)
      message(drug_name, "has been approved using the Accelerated Approval Strategy.")
    }
  )
)

# Context
DrugApprovalContext <- setRefClass(
  "DrugApprovalContext",
  fields = list(strategy = "RegulatoryStrategy"),
  methods = list(
    set_strategy = function(new_strategy) {
      strategy <<- new_strategy
    },
    approve_drug = function(drug_name) {
      strategy$approve_application(drug_name)
    }
  )
)

approval_context <- DrugApprovalContext$new()

# Set Standard Approval Strategy
standard_strategy <- StandardApprovalStrategy$new()
approval_context$set_strategy(standard_strategy)
approval_context$approve_drug("Test Small Molecule 01")

# Set Accelerated Approval Strategy
accelerated_strategy <- AcceleratedApprovalStrategy$new()
approval_context$set_strategy(accelerated_strategy)
approval_context$approve_drug("Test Small Molecule 02")


# Define the Subject Interface
DrugApprovalProcess <- setRefClass(
  "DrugApprovalProcess",
  methods = list(
    apply_for_approval = function(drug_name) {
      stop("This method should be overridden in subclasses")
    }
  )
)

# RealSubject Class
RealDrugApprovalProcess <- setRefClass(
  "RealDrugApprovalProcess",
  contains = "DrugApprovalProcess",
  methods = list(
    apply_for_approval = function(drug_name) {
      message("Processing approval for drug:", drug_name)
    }
  )
)

# Proxy Class
DrugApprovalProxy <- setRefClass(
  "DrugApprovalProxy",
  contains = "DrugApprovalProcess",
  fields = list(
    real_subject = "DrugApprovalProcess"
  ),
  methods = list(
    initialize = function() {
      real_subject <<- RealDrugApprovalProcess$new()
    },
    check_authorization = function() {
      message("Checking authorization...")
      return(TRUE)
    },
    apply_for_approval = function(drug_name) {
      if (check_authorization()) {
        real_subject$apply_for_approval(drug_name)
      } else {
        message("Unauthorized access")
      }
    }
  )
)

request_approval <- function(proxy, drug_type) {
  message("\nRequesting approval for ", drug_type, "...")
  proxy$apply_for_approval(drug_type)
}

# Create a Proxy instance
proxy <- DrugApprovalProxy$new()

request_approval(proxy,"Test Vaccine 01")
request_approval(proxy,"Test Small Molecule 01")
request_approval(proxy,"Test Small Molecule 01")

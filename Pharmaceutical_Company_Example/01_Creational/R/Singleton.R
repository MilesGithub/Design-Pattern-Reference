# Singleton
RegulatoryApprovalSystem <- local({
  instance <- NULL
  
  RegulatoryApprovalSystemClass <- setRefClass(
    "RegulatoryApprovalSystem",
    fields = list(
      approvals = "list"
    ),
    methods = list(
      add_approval = function(drug_name, status) {
        approvals[[drug_name]] <<- status
        cat("Added approval status for:", drug_name, "- Status:", status, "\n")
      },
      get_status = function(drug_name) {
        if (!is.null(approvals[[drug_name]])) {
          cat("Approval status for", drug_name, "is:", approvals[[drug_name]], "\n")
        } else {
          cat("No approval status found for", drug_name, "\n")
        }
      },
      show_all_approvals = function() {
        cat("Current approval statuses:\n")
        for (drug in names(approvals)) {
          cat(drug, ":", approvals[[drug]], "\n")
        }
      }
    )
  )
  
  function() {
    if (is.null(instance)) {
      instance <<- RegulatoryApprovalSystemClass$new(approvals = list())
    }
    return(instance)
  }
})

# Get single instance of RegulatoryApprovalSystem
approval_system <- RegulatoryApprovalSystem()

# Add approvals
approval_system$add_approval("Test Vaccine 01", "Approved")
approval_system$add_approval("Test Small Molecule 01", "Under Review")
approval_system$add_approval("Test Monoclonal Antibody 01", "Approved")

approval_system$get_status("Test Small Molecule 01")
approval_system$get_status("Test Vaccine 01")

approval_system$show_all_approvals()

# Create another instance (it will return the same instance)
approval_system_2 <- RegulatoryApprovalSystem()
approval_system_2$add_approval("Test Small Molecule 02", "Pending Review")

# Two instances are the same
approval_system_2$show_all_approvals()
approval_system$show_all_approvals()

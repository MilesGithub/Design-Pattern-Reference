# Command Interface
RegulatoryCommand <- setRefClass(
  "RegulatoryCommand",
  methods = list(
    execute = function() {
      stop("This method should be overridden!")
    }
  )
)

# Concrete Command: Submit Drug Application
SubmitApplicationCommand <- setRefClass(
  "SubmitApplicationCommand",
  contains = "RegulatoryCommand",
  fields = list(drug_name = "character", system = "ANY"),
  methods = list(
    execute = function() {
      system$submit_application(drug_name)
    }
  )
)

# Concrete Command: Approve Drug
ApproveDrugCommand <- setRefClass(
  "ApproveDrugCommand",
  contains = "RegulatoryCommand",
  fields = list(drug_name = "character", system = "ANY"),
  methods = list(
    execute = function() {
      system$approve_drug(drug_name)
    }
  )
)

# Concrete Command: Reject Drug
RejectDrugCommand <- setRefClass(
  "RejectDrugCommand",
  contains = "RegulatoryCommand",
  fields = list(drug_name = "character", system = "ANY"),
  methods = list(
    execute = function() {
      system$reject_drug(drug_name)
    }
  )
)

# Receiver
RegulatorySystem <- setRefClass(
  "RegulatorySystem",
  fields = list(applications = "list", status = "list"),
  methods = list(
    submit_application = function(drug_name) {
      applications[[drug_name]] <- TRUE
      status[[drug_name]] <- "Submitted"
      message("Application submitted for:", drug_name)
    },
    approve_drug = function(drug_name) {
      if (!is.null(applications[[drug_name]])) {
        status[[drug_name]] <- "Approved"
        message(drug_name, "approved.\n")
      } else {
        message("No application found for:", drug_name)
      }
    },
    reject_drug = function(drug_name) {
      if (!is.null(applications[[drug_name]])) {
        status[[drug_name]] <- "Rejected"
        message(drug_name, "rejected.\n")
      } else {
        message("No application found for:", drug_name)
      }
    },
    show_status = function(drug_name) {
      if (!is.null(status[[drug_name]])) {
        message("Current status of", drug_name, ":", status[[drug_name]])
      } else {
        message("No status found for:", drug_name)
      }
    }
  )
)

# Invoker
ApprovalSystemInvoker <- setRefClass(
  "ApprovalSystemInvoker",
  fields = list(commands = "list"),
  methods = list(
    add_command = function(command) {
      commands[[length(commands) + 1]] <<- command
    },
    execute_commands = function() {
      for (command in commands) {
        command$execute()
      }
      commands <<- list()  # Clear the command queue after execution
    }
  )
)

# Create Receiver
regulatory_system <- RegulatorySystem$new()

# Create Invoker
approval_system_invoker <- ApprovalSystemInvoker$new()

# Add commands to invoker
submit_vaccine_command <- SubmitApplicationCommand$new(drug_name = "Test Small Molecule 01", system = regulatory_system)
approve_vaccine_command <- ApproveDrugCommand$new(drug_name = "Test Small Molecule 01", system = regulatory_system)
reject_aspirin_command <- RejectDrugCommand$new(drug_name = "Test Small Molecule 02", system = regulatory_system)

approval_system_invoker$add_command(submit_vaccine_command)
approval_system_invoker$add_command(approve_vaccine_command)
approval_system_invoker$add_command(reject_aspirin_command)

approval_system_invoker$execute_commands()

# Show the status of drugs after executing commands
regulatory_system$show_status("Test Small Molecule 01")
regulatory_system$show_status("Test Small Molecule 02")

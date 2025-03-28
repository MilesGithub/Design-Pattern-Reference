# Abstract Factory Interface
RegulatoryFactory <- setRefClass(
  "RegulatoryFactory",
  methods = list(
    create_submission_form = function() {
      stop("This method must be overridden")
    },
    create_testing_protocol = function() {
      stop("This method must be overridden")
    }
  )
)

# Concrete Factory for Vaccines
VaccineRegulatoryFactory <- setRefClass(
  "VaccineRegulatoryFactory",
  contains = "RegulatoryFactory",
  methods = list(
    create_submission_form = function() {
      return(VaccineSubmissionForm$new())
    },
    create_testing_protocol = function() {
      return(VaccineTestingProtocol$new())
    }
  )
)

# Concrete Factory for Small-Molecule Drugs
SmallMoleculeRegulatoryFactory <- setRefClass(
  "SmallMoleculeRegulatoryFactory",
  contains = "RegulatoryFactory",
  methods = list(
    create_submission_form = function() {
      return(SmallMoleculeSubmissionForm$new())
    },
    create_testing_protocol = function() {
      return(SmallMoleculeTestingProtocol$new())
    }
  )
)

# Concrete Factory for Biologics
BiologicsRegulatoryFactory <- setRefClass(
  "BiologicsRegulatoryFactory",
  contains = "RegulatoryFactory",
  methods = list(
    create_submission_form = function() {
      return(BiologicsSubmissionForm$new())
    },
    create_testing_protocol = function() {
      return(BiologicsTestingProtocol$new())
    }
  )
)

# Abstract Product
SubmissionForm <- setRefClass(
  "SubmissionForm",
  methods = list(
    submit = function() {
      stop("This method must be overridden by a subclass!")
    }
  )
)

# Concrete Product: Vaccine Submission Form
VaccineSubmissionForm <- setRefClass(
  "VaccineSubmissionForm",
  contains = "SubmissionForm",
  methods = list(
    submit = function() {
      message("Submitting vaccine clinical trial data form.")
    }
  )
)

# Concrete Product: Small-Molecule Submission Form
SmallMoleculeSubmissionForm <- setRefClass(
  "SmallMoleculeSubmissionForm",
  contains = "SubmissionForm",
  methods = list(
    submit = function() {
      message("Submitting small-molecule drug trial data form.")
    }
  )
)

# Concrete Product: Biologics Submission Form
BiologicsSubmissionForm <- setRefClass(
  "BiologicsSubmissionForm",
  contains = "SubmissionForm",
  methods = list(
    submit = function() {
      message("Submitting biologics clinical trial data form.")
    }
  )
)

# Abstract Product
TestingProtocol <- setRefClass(
  "TestingProtocol",
  methods = list(
    run_tests = function() {
      stop("This method must be overridden by a subclass!")
    }
  )
)

# Concrete Product: Vaccine Testing Protocol
VaccineTestingProtocol <- setRefClass(
  "VaccineTestingProtocol",
  contains = "TestingProtocol",
  methods = list(
    run_tests = function() {
      message("Running tests for vaccines.")
    }
  )
)

# Concrete Product: Small-Molecule Testing Protocol
SmallMoleculeTestingProtocol <- setRefClass(
  "SmallMoleculeTestingProtocol",
  contains = "TestingProtocol",
  methods = list(
    run_tests = function() {
      message("Running tests for small-molecule drugs.")
    }
  )
)

# Concrete Product: Biologics Testing Protocol
BiologicsTestingProtocol <- setRefClass(
  "BiologicsTestingProtocol",
  contains = "TestingProtocol",
  methods = list(
    run_tests = function() {
      message("Running tests for biologics.")
    }
  )
)

# Client Code: Regulatory Process
process_regulatory_approval <- function(factory) {
  submission_form <- factory$create_submission_form()
  testing_protocol <- factory$create_testing_protocol()
  
  submission_form$submit()
  testing_protocol$run_tests()
}

# Vaccine Regulatory Process
vaccine_factory <- VaccineRegulatoryFactory$new()
process_regulatory_approval(vaccine_factory)

# Small-Molecule Drug Regulatory Process
small_molecule_factory <- SmallMoleculeRegulatoryFactory$new()
process_regulatory_approval(small_molecule_factory)

# Biologics Regulatory Process
biologics_factory <- BiologicsRegulatoryFactory$new()
process_regulatory_approval(biologics_factory)

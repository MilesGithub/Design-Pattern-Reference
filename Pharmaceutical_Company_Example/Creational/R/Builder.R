# Product
RegulatoryDocument <- setRefClass(
  "RegulatoryDocument",
  fields = list(
    drug_name = "character",
    clinical_trial_data = "character",
    safety_report = "character",
    manufacturing_data = "character"
  ),
  methods = list(
    show_document = function() {
      cat("Regulatory Document for:", drug_name, "\n",
          "Clinical Trial Data: ", clinical_trial_data, "\n",
          "Safety Report: ", safety_report, "\n",
          "Manufacturing Data: ", manufacturing_data, "\n\n")
    }
  )
)

# Abstract Builder
RegulatoryDocumentBuilder <- setRefClass(
  "RegulatoryDocumentBuilder",
  fields = list(
    document = "ANY"
  ),
  methods = list(
    initialize = function(drug_name) {
      .self$document <- RegulatoryDocument$new(drug_name = drug_name)
    },
    add_clinical_trial_data = function() {
      stop("This method must be overridden by a concrete builder")
    },
    add_safety_report = function() {
      stop("This method must be overridden by a concrete builder")
    },
    add_manufacturing_data = function() {
      stop("This method must be overridden by a concrete builder")
    },
    get_document = function() {
      return(.self$document)
    }
  )
)

# Concrete Builder for Vaccines
VaccineDocumentBuilder <- setRefClass(
  "VaccineDocumentBuilder",
  contains = "RegulatoryDocumentBuilder",
  methods = list(
    add_clinical_trial_data = function() {
      .self$document$clinical_trial_data <- "Vaccine clinical trial data"
    },
    add_safety_report = function() {
      .self$document$safety_report <- "Vaccine safety report"
    },
    add_manufacturing_data = function() {
      .self$document$manufacturing_data <- "Vaccine manufacturing data"
    }
  )
)

# Concrete Builder for Small-Molecule Drugs
SmallMoleculeDocumentBuilder <- setRefClass(
  "SmallMoleculeDocumentBuilder",
  contains = "RegulatoryDocumentBuilder",
  methods = list(
    add_clinical_trial_data = function() {
      .self$document$clinical_trial_data <- "Small-molecule clinical trial data"
    },
    add_safety_report = function() {
      .self$document$safety_report <- "Small-molecule safety report"
    },
    add_manufacturing_data = function() {
      .self$document$manufacturing_data <- "Small-molecule manufacturing data"
    }
  )
)

# Concrete Builder for Biologics
BiologicsDocumentBuilder <- setRefClass(
  "BiologicsDocumentBuilder",
  contains = "RegulatoryDocumentBuilder",
  methods = list(
    add_clinical_trial_data = function() {
      .self$document$clinical_trial_data <- "Biologics clinical trial data"
    },
    add_safety_report = function() {
      .self$document$safety_report <- "Biologics safety report"
    },
    add_manufacturing_data = function() {
      .self$document$manufacturing_data <- "Biologics manufacturing data"
    }
  )
)

# Director: Manages the building process
RegulatoryDirector <- setRefClass(
  "RegulatoryDirector",
  fields = list(
    builder = "ANY"
  ),
  methods = list(
    initialize = function(builder) {
      .self$builder <- builder
    },
    construct_document = function() {
      .self$builder$add_clinical_trial_data()
      .self$builder$add_safety_report()
      .self$builder$add_manufacturing_data()
    },
    get_document = function() {
      return(.self$builder$get_document())
    }
  )
)

# Create a director for a Vaccine regulatory document
vaccine_builder <- VaccineDocumentBuilder$new("Test Vaccine 01")
director <- RegulatoryDirector$new(vaccine_builder)
director$construct_document()
vaccine_doc <- director$get_document()
vaccine_doc$show_document()

# Create a director for a Small-Molecule regulatory document
small_molecule_builder <- SmallMoleculeDocumentBuilder$new("Test Small Molecule 01")
director <- RegulatoryDirector$new(small_molecule_builder)
director$construct_document()
small_molecule_doc <- director$get_document()
small_molecule_doc$show_document()

# Create a director for a Biologics regulatory document
biologics_builder <- BiologicsDocumentBuilder$new("Test Monoclonal Antibody 01")
director <- RegulatoryDirector$new(biologics_builder)
director$construct_document()
biologics_doc <- director$get_document()
biologics_doc$show_document()

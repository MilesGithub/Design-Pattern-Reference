# Prototype
RegulatoryDocumentPrototype <- setRefClass(
  "RegulatoryDocumentPrototype",
  fields = list(
    drug_name = "character",
    document_type = "character",
    clinical_trial_data = "character",
    safety_report = "character",
    manufacturing_data = "character"
  ),
  methods = list(
    clone_document = function(new_drug_name) {
      cloned_document <- RegulatoryDocumentPrototype$new(
        drug_name = new_drug_name,
        document_type = .self$document_type,
        clinical_trial_data = .self$clinical_trial_data,
        safety_report = .self$safety_report,
        manufacturing_data = .self$manufacturing_data
      )
      return(cloned_document)
    },
    show_document = function() {
      cat("Regulatory Document for:", drug_name, "\n",
          "Document Type: ", document_type, "\n",
          "Clinical Trial Data: ", clinical_trial_data, "\n",
          "Safety Report: ", safety_report, "\n",
          "Manufacturing Data: ", manufacturing_data, "\n\n")
    }
  )
)

vaccine_prototype <- RegulatoryDocumentPrototype$new(
  drug_name = "Vaccine Prototype",
  document_type = "Vaccine Regulatory Document",
  clinical_trial_data = "Standard vaccine clinical trial data",
  safety_report = "Standard vaccine safety report",
  manufacturing_data = "Standard vaccine manufacturing data"
)

small_molecule_prototype <- RegulatoryDocumentPrototype$new(
  drug_name = "Small-Molecule Prototype",
  document_type = "Small-Molecule Regulatory Document",
  clinical_trial_data = "Standard small-molecule clinical trial data",
  safety_report = "Standard small-molecule safety report",
  manufacturing_data = "Standard small-molecule manufacturing data"
)

biologics_prototype <- RegulatoryDocumentPrototype$new(
  drug_name = "Biologics Prototype",
  document_type = "Biologics Regulatory Document",
  clinical_trial_data = "Standard biologics clinical trial data",
  safety_report = "Standard biologics safety report",
  manufacturing_data = "Standard biologics manufacturing data"
)


# Clone the vaccine prototype for a new vaccine
new_vaccine_document <- vaccine_prototype$clone_document("Test Vaccine 01")
new_vaccine_document$show_document()

# Clone the small-molecule prototype for a new drug
new_small_molecule_document <- small_molecule_prototype$clone_document("Test Small Molecule 01")
new_small_molecule_document$show_document()

# Clone the biologics prototype for a new biologic drug
new_biologics_document <- biologics_prototype$clone_document("Test Monoclonal Antibody 01")
new_biologics_document$show_document()

# Adaptee
ClinicalTrialSystem <- setRefClass(
  "ClinicalTrialSystem",
  fields = list(
    trial_data = "character"
  ),
  methods = list(
    initialize = function(drug_name) {
      .self$trial_data <- paste(drug_name, "clinical trial data")
    },
    get_trial_data = function() {
      return(.self$trial_data)
    }
  )
)

# Target
RegulatoryAPI <- setRefClass(
  "RegulatoryAPI",
  methods = list(
    upload_data_to_regulator = function(data) {
      message("Uploading the following data to regulatory authorities: ", data)
    }
  )
)

# Adapter to bridge between ClinicalTrialSystem (Adaptee) and RegulatoryAPI (Target)
RegulatoryAdapter <- setRefClass(
  "RegulatoryAdapter",
  fields = list(
    clinical_trial_system = "ANY",
    regulatory_api = "ANY"
  ),
  methods = list(
    initialize = function(clinical_trial_system, regulatory_api) {
      .self$clinical_trial_system <- clinical_trial_system
      .self$regulatory_api <- regulatory_api
    },
    submit_trial_data = function() {
      trial_data <- .self$clinical_trial_system$get_trial_data()
      .self$regulatory_api$upload_data_to_regulator(trial_data)
    }
  )
)


clinical_system_1 <- ClinicalTrialSystem$new("Test Small Molecule 01")
clinical_system_2 <- ClinicalTrialSystem$new("Test Small Molecule 02")
regulatory_api <- RegulatoryAPI$new()

adapter_1 <- RegulatoryAdapter$new(clinical_system_1, regulatory_api)
adapter_1$submit_trial_data()

adapter_2 <- RegulatoryAdapter$new(clinical_system_2, regulatory_api)
adapter_2$submit_trial_data()




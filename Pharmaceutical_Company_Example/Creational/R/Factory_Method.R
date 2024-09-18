# Product
RegulatoryDocument <- setRefClass(
  "RegulatoryDocument",
  fields = list(
    drug_name = "character",
    document_type = "character"
  ),
  methods = list(
    show_document = function() {
      cat("Regulatory Document for:", drug_name, "\n",
          "Type of Document: ", document_type, "\n\n")
    }
  )
)

# Abstract Creator
RegulatoryDocumentFactory <- setRefClass(
  "RegulatoryDocumentFactory",
  methods = list(
    create_document = function(drug_name) {
      stop("This method must be overridden by a concrete factory!")
    }
  )
)

# Concrete Creator for Vaccine Documents
VaccineDocumentFactory <- setRefClass(
  "VaccineDocumentFactory",
  contains = "RegulatoryDocumentFactory",
  methods = list(
    create_document = function(drug_name) {
      return(RegulatoryDocument$new(drug_name = drug_name, document_type = "Vaccine Regulatory Document"))
    }
  )
)

# Concrete Creator for Small-Molecule Documents
SmallMoleculeDocumentFactory <- setRefClass(
  "SmallMoleculeDocumentFactory",
  contains = "RegulatoryDocumentFactory",
  methods = list(
    create_document = function(drug_name) {
      return(RegulatoryDocument$new(drug_name = drug_name, document_type = "Small-Molecule Regulatory Document"))
    }
  )
)

# Concrete Creator for Biologics Documents
BiologicsDocumentFactory <- setRefClass(
  "BiologicsDocumentFactory",
  contains = "RegulatoryDocumentFactory",
  methods = list(
    create_document = function(drug_name) {
      return(RegulatoryDocument$new(drug_name = drug_name, document_type = "Biologics Regulatory Document"))
    }
  )
)

process_document <- function(factory, drug_name) {
  document <- factory$create_document(drug_name)
  document$show_document()
}

vaccine_factory <- VaccineDocumentFactory$new()
process_document(vaccine_factory, "Test Vaccine 01")

small_molecule_factory <- SmallMoleculeDocumentFactory$new()
process_document(small_molecule_factory, "Test Small Molecule 01")

biologics_factory <- BiologicsDocumentFactory$new()
process_document(biologics_factory, "Test Monoclonal Antibody 01")

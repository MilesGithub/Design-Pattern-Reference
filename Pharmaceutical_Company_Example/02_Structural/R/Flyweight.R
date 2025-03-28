# Flyweight class
RegulatoryProcessFlyweight <- setRefClass(
  "RegulatoryProcessFlyweight",
  fields = list(
    common_regulatory_steps = "list"
  ),
  methods = list(
    initialize = function() {
      .self$common_regulatory_steps <- list(
        "Submit Trial Data",
        "Review Trial Data",
        "Submit Safety Data",
        "Review Safety Data",
        "Submit Regulatory Documents",
        "Obtain Regulatory Approval"
      )
    },
    get_steps = function() {
      return(.self$common_regulatory_steps)
    }
  )
)

# Flyweight Factory
FlyweightFactory <- setRefClass(
  "FlyweightFactory",
  fields = list(
    flyweights = "list"
  ),
  methods = list(
    get_flyweight = function(key) {
      if (!key %in% names(.self$flyweights)) {
        message("Creating new flyweight for: ", key)
        flyweight <- RegulatoryProcessFlyweight$new()
        .self$flyweights[[key]] <- flyweight
      } else {
        message("Reusing existing flyweight for: ", key)
      }
      return(.self$flyweights[[key]])
    }
  )
)

# Uses flyweights for shared regulatory processes
Drug <- setRefClass(
  "Drug",
  fields = list(
    name = "character",
    regulatory_steps = "list",
    flyweight = "ANY"
  ),
  methods = list(
    initialize = function(name, flyweight) {
      .self$name <- name
      .self$flyweight <- flyweight
      .self$regulatory_steps <- flyweight$get_steps()
    },
    display_regulatory_process = function() {
      message("Regulatory process for ", .self$name, ":")
      for (step in .self$regulatory_steps) {
        message(" - ", step)
      }
    }
  )
)


flyweight_factory <- FlyweightFactory$new()

drug1 <- Drug$new("Test Small Molecule 01", flyweight_factory$get_flyweight("Standard Process"))
drug2 <- Drug$new("Test Small Molecule 02", flyweight_factory$get_flyweight("Standard Process"))
drug3 <- Drug$new("Test Monoclonal Antibody 01", flyweight_factory$get_flyweight("Standard Process"))

drug1$display_regulatory_process()
drug2$display_regulatory_process()
drug3$display_regulatory_process()

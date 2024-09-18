# Iterator Interface
ApplicationIterator <- setRefClass(
  "ApplicationIterator",
  methods = list(
    has_next = function() {
      stop("This method should be overridden!")
    },
    is_next = function() {
      stop("This method should be overridden!")
    }
  )
)

# Concrete Iterator
DrugApplicationIterator <- setRefClass(
  "DrugApplicationIterator",
  contains = "ApplicationIterator",
  fields = list(
    applications = "list",
    position = "numeric"
  ),
  methods = list(
    initialize = function(applications) {
      .self$applications <- applications
      .self$position <- 1
    },
    has_next = function() {
      return(position <= length(applications))
    },
    is_next = function() {
      if (has_next()) {
        app <- applications[[position]]
        position <<- position + 1
        return(app)
      } else {
        return(NULL)
      }
    }
  )
)

# Aggregate Interface
ApplicationCollection <- setRefClass(
  "ApplicationCollection",
  methods = list(
    create_iterator = function() {
      stop("This method should be overridden!")
    }
  )
)

# Concrete Aggregate
DrugApplicationCollection <- setRefClass(
  "DrugApplicationCollection",
  contains = "ApplicationCollection",
  fields = list(applications = "list"),
  methods = list(
    add_application = function(application) {
      applications[[length(applications) + 1]] <<- application
    },
    create_iterator = function() {
      return(DrugApplicationIterator$new(applications = applications))
    }
  )
)

drug_collection <- DrugApplicationCollection$new()

drug_collection$add_application(list(drug_name = "Test Vaccine 01", status = "Under Review"))
drug_collection$add_application(list(drug_name = "Test Small Molecule 01", status = "Approved"))
drug_collection$add_application(list(drug_name = "Test Monoclonal Antibody 01", status = "Rejected"))

iterator <- drug_collection$create_iterator()

# Use the iterator to traverse the applications
while (iterator$has_next()) {
  application <- iterator$is_next()
  message("Drug Name:", application$drug_name, "- Status:", application$status)
}

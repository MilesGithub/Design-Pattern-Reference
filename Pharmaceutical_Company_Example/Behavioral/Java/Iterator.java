import java.util.List;
import java.util.ArrayList;
import java.util.Map;

// Iterator Interface
interface ApplicationIterator {
    boolean hasNext();
    Map<String, String> next();
}

// Concrete Iterator
class DrugApplicationIterator implements ApplicationIterator {
    private List<Map<String, String>> applications;
    private int position;

    public DrugApplicationIterator(List<Map<String, String>> applications) {
        this.applications = applications;
        this.position = 0;
    }

    @Override
    public boolean hasNext() {
        return position < applications.size();
    }

    @Override
    public Map<String, String> next() {
        if (hasNext()) {
            Map<String, String> app = applications.get(position);
            position++;
            return app;
        }
        return null;
    }
}

// Aggregate Interface
interface ApplicationCollection {
    ApplicationIterator createIterator();
}

// Concrete Aggregate
class DrugApplicationCollection implements ApplicationCollection {
    private List<Map<String, String>> applications;

    public DrugApplicationCollection() {
        this.applications = new ArrayList<>();
    }

    public void addApplication(Map<String, String> application) {
        applications.add(application);
    }

    @Override
    public ApplicationIterator createIterator() {
        return new DrugApplicationIterator(applications);
    }
}

public class Main {
    public static void main(String[] args) {
        DrugApplicationCollection drugCollection = new DrugApplicationCollection();
        
        // Adding applications
        drugCollection.addApplication(Map.of("drug_name", "Test Vaccine 01", "status", "Under Review"));
        drugCollection.addApplication(Map.of("drug_name", "Test Small Molecule 01", "status", "Approved"));
        drugCollection.addApplication(Map.of("drug_name", "Test Monoclonal Antibody 01", "status", "Rejected"));
        
        // Create the iterator
        ApplicationIterator iterator = drugCollection.createIterator();
        
        // Use the iterator to traverse the applications
        while (iterator.hasNext()) {
            Map<String, String> application = iterator.next();
            if (application != null) {
                System.out.println("Drug Name: " + application.get("drug_name") + " - Status: " + application.get("status"));
            }
        }
    }
}

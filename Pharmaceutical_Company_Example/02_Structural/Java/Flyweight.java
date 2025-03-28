import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;

// Flyweight class
class RegulatoryProcessFlyweight {
    private List<String> commonRegulatorySteps;

    public RegulatoryProcessFlyweight() {
        commonRegulatorySteps = new ArrayList<>();
        commonRegulatorySteps.add("Submit Trial Data");
        commonRegulatorySteps.add("Review Trial Data");
        commonRegulatorySteps.add("Submit Safety Data");
        commonRegulatorySteps.add("Review Safety Data");
        commonRegulatorySteps.add("Submit Regulatory Documents");
        commonRegulatorySteps.add("Obtain Regulatory Approval");
    }

    public List<String> getSteps() {
        return commonRegulatorySteps;
    }
}

// Flyweight Factory
class FlyweightFactory {
    private Map<String, RegulatoryProcessFlyweight> flyweights;

    public FlyweightFactory() {
        flyweights = new HashMap<>();
    }

    public RegulatoryProcessFlyweight getFlyweight(String key) {
        if (!flyweights.containsKey(key)) {
            System.out.println("Creating new flyweight for: " + key);
            RegulatoryProcessFlyweight flyweight = new RegulatoryProcessFlyweight();
            flyweights.put(key, flyweight);
        } else {
            System.out.println("Reusing existing flyweight for: " + key);
        }
        return flyweights.get(key);
    }
}

// Uses flyweights for shared regulatory processes
class Drug {
    private String name;
    private RegulatoryProcessFlyweight flyweight;
    private List<String> regulatorySteps;

    public Drug(String name, RegulatoryProcessFlyweight flyweight) {
        this.name = name;
        this.flyweight = flyweight;
        this.regulatorySteps = flyweight.getSteps();
    }

    public void displayRegulatoryProcess() {
        System.out.println("Regulatory process for " + name + ":");
        for (String step : regulatorySteps) {
            System.out.println(" - " + step);
        }
    }
}

public class FlyweightExample {
    public static void main(String[] args) {
        FlyweightFactory flyweightFactory = new FlyweightFactory();

        Drug drug1 = new Drug("Test Small Molecule 01", flyweightFactory.getFlyweight("Standard Process"));
        Drug drug2 = new Drug("Test Small Molecule 02", flyweightFactory.getFlyweight("Standard Process"));
        Drug drug3 = new Drug("Test Monoclonal Antibody 01", flyweightFactory.getFlyweight("Standard Process"));

        drug1.displayRegulatoryProcess();
        drug2.displayRegulatoryProcess();
        drug3.displayRegulatoryProcess();
    }
}

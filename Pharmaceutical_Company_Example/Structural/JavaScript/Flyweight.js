// Flyweight class
class RegulatoryProcessFlyweight {
    constructor() {
        this.commonRegulatorySteps = [
            "Submit Trial Data",
            "Review Trial Data",
            "Submit Safety Data",
            "Review Safety Data",
            "Submit Regulatory Documents",
            "Obtain Regulatory Approval"
        ];
    }

    getSteps() {
        return this.commonRegulatorySteps;
    }
}

// Flyweight Factory
class FlyweightFactory {
    constructor() {
        this.flyweights = {};
    }

    getFlyweight(key) {
        if (!(key in this.flyweights)) {
            console.log(`Creating new flyweight for: ${key}`);
            const flyweight = new RegulatoryProcessFlyweight();
            this.flyweights[key] = flyweight;
        } else {
            console.log(`Reusing existing flyweight for: ${key}`);
        }
        return this.flyweights[key];
    }
}

// Uses flyweights for shared regulatory processes
class Drug {
    constructor(name, flyweight) {
        this.name = name;
        this.flyweight = flyweight;
        this.regulatorySteps = flyweight.getSteps();
    }

    displayRegulatoryProcess() {
        console.log(`Regulatory process for ${this.name}:`);
        this.regulatorySteps.forEach(step => {
            console.log(` - ${step}`);
        });
    }
}

// Usage example
const flyweightFactory = new FlyweightFactory();

const drug1 = new Drug("Test Small Molecule 01", flyweightFactory.getFlyweight("Standard Process"));
const drug2 = new Drug("Test Small Molecule 02", flyweightFactory.getFlyweight("Standard Process"));
const drug3 = new Drug("Test Monoclonal Antibody 01", flyweightFactory.getFlyweight("Standard Process"));

drug1.displayRegulatoryProcess();
drug2.displayRegulatoryProcess();
drug3.displayRegulatoryProcess();

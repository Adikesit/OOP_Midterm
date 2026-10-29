public class Washer {
    private final String id;
    private final double capacityKg;

    public Washer(String id, double capacityKg) {
        // TODO(Q033): store id and capacityKg.
        this.id = id;
        this.capacityKg = capacityKg;
    }

    public String getId() {
        return id;
    }

    /** Loads a bag; throws OverloadException if it is heavier than the capacity. */
    public void load(double kg) throws OverloadException {
        // TODO(Q033): kg <= 0 → throw new IllegalArgumentException(...);
        //   kg > capacityKg → throw new OverloadException(id, kg, capacityKg);
        //   otherwise print loaded message.
        if (kg <= 0) {
            throw new IllegalArgumentException("Must be positive");
        }
        
        if (kg > capacityKg) {
            throw new OverloadException(id, kg, capacityKg);
        }
        System.out.println("  " + id + " loaded " + kg + " kg");
    }
}

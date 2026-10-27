public class Dryer extends Machine {
    public Dryer(String id, double capacityKg) {
        super(id, capacityKg);
    }

    @Override
    protected int cycleMinutes(double kg) {
        // TODO(Q050): kg <= 5 ? 50 : 70
        return kg <= 5 ? 50 : 70;
    }
}

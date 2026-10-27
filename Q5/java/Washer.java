public class Washer extends Machine {
    public Washer(String id, double capacityKg) {
        super(id, capacityKg);
    }

    @Override
    protected int cycleMinutes(double kg) {
        // TODO(Q050): 30 minutes plus 3 per started kilogram
        return 30 + (int) Math.ceil(kg) * 3;
    }
}

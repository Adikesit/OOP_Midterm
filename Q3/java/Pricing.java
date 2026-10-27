public class Pricing {
    static final long RATE = 7000;             // Wash & Fold, rupiah per kilogram
    static final double MINIMUM_KG = 3.0;

    /** Price of one Wash & Fold bag: minimum 3 kg, rounded up to 0.5 kg, express +50%, members -10%. */
    public static long price(double kg, boolean express, boolean member) {
        if (kg <= 0) {
            throw new IllegalArgumentException("weight must be positive: " + kg);
        }
        // TODO(Q040): round UP to the next 0.5 kg (3.01 → 3.5, 3.5 → 3.5, 3.51 → 4.0).
        //   Hint: Math.ceil(Math.max(kg, MINIMUM_KG) * 2) / 2 — NOT Math.round(... * 2) / 2.0.
        double charged = Math.ceil(Math.max(kg, MINIMUM_KG) * 2) / 2;
        long total = Math.round(charged * RATE);
        if (express) {
            total = total * 3 / 2;
        }
        if (member) {
            total -= total / 10;
        }
        return total;
    }
}

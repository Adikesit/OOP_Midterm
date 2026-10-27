class OverloadError(Exception):
    """A machine was asked to take more than it can hold."""

    def __init__(self, machine_id, requested_kg, capacity_kg):
        # TODO(Q033): call super().__init__(f"...") and store the fields.
        super().__init__(f"{machine_id} cannot take {requested_kg:.1f} kg (capacity {capacity_kg:.1f} kg)")
        self.machine_id = machine_id
        self.excess_kg = requested_kg - capacity_kg


class Washer:
    def __init__(self, machine_id, capacity_kg):
        # TODO(Q033): store machine_id and capacity_kg.
        self.machine_id = machine_id
        self.capacity_kg = capacity_kg

    def load(self, kg):
        """Loads a bag; raises OverloadError if it is heavier than the capacity."""
        # TODO(Q033): kg <= 0 → raise ValueError(...);
        #   kg > self.capacity_kg → raise OverloadError(self.machine_id, kg, self.capacity_kg);
        #   otherwise print loaded message.
        if kg <= 0:
            raise ValueError(f"weight must be positive: {kg}")
        if kg > self.capacity_kg:
            raise OverloadError(self.machine_id, kg, self.capacity_kg)
        print(f"  {self.machine_id} loaded {kg} kg")

def place(washers, kg):
    """Tries each washer in turn; returns the id of the one that took the bag, or None."""
    for w in washers:
        # TODO(Q033): try w.load(kg); return w.machine_id; except OverloadError as e: print(...)
        try:
            w.load(kg)
            return w.machine_id
        except OverloadError as e:
            print(f"  {e}, {e.excess_kg:.1f} kg too much")
    return None


washers = [Washer("W1", 7.0), Washer("W2", 10.0), Washer("W3", 15.0)]
for kg in [6.5, 12.0, 18.0]:
    where = place(washers, kg)
    print(f"{kg} kg -> {where if where is not None else 'split the bag'}")
try:
    washers[0].load(-2)
except OverloadError:
    print("not reached")

def total(a):
    # TODO(Q026): sum all elements of a.
    s = 0.0
    for i in range(len(a)):
        s += a[i]
    return s


def average(a):
    # TODO(Q026): total(a) / len(a).
    return total(a) / len(a)


def index_of_max(a):
    """Index of the largest element; the first one if several are equal."""
    # TODO(Q026): best = 0; loop i from 1; if a[i] > a[best], best = i.
    best = 0
    for i in range(1, len(a)):
        if a[i] > a[best]:
            best = i
    return best


def count_above(a, limit):
    # TODO(Q026): count elements strictly greater than limit.
    count = 0
    for i in range(len(a)):
        if a[i] > limit:
            count += 1
    return count


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
kg = [42.5, 38.0, 51.5, 47.0, 60.5, 72.0, 35.5]

avg = average(kg)
busiest = index_of_max(kg)
print(f"total {total(kg):.1f} kg, average {avg:.2f} kg")
print(f"busiest day: {days[busiest]} ({kg[busiest]} kg)")
print("days above average:", count_above(kg, avg))

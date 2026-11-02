def estimate_1rm(weight, reps):
    """Estimate a one-rep max using the Epley formula."""
    return round(weight * (1 + reps / 30), 1)


def kg_to_lb(kg):
    """Convert kilograms to pounds."""
    return round(kg * 2.20462, 1)

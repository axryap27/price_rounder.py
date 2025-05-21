def advanced_round(rules: dict, price: float) -> float:
    # Find which rule applies for this price
    #iterates through the list rounding_rules where each element is a dictionary
    for rule in rules.get("rounding_rules", []):
        min_price = rule.get("min", float('-inf'))          #finds minimum price in range
        max_price = rule.get("max", float('inf'))           #finds max price in range
        if min_price <= price < max_price:
            # Found the right rule, now apply it
            endings = rule["endings"]
            break
    else:
        #price of good is out of bounds
        print(f"No rule matches the price: {price}")

    # Try all the endings and pick whichever is closest
    closest_price = None
    smallest_diff = float('inf')

    for ending in endings:
        base = int(price)
        candidate = base + ending
        diff = abs(price - candidate)
        if diff < smallest_diff:
            smallest_diff = diff
            closest_price = candidate

    # Round the final result to 2 decimal places
    return round(closest_price, 2)

rules1 = {
        "rounding_rules": [
            {"max": 10, "endings": [0.99, 0.49]},
            {"min": 10, "max": 100, "endings": [0.00, 5.00]},
            {"min": 100, "endings": [10.00]}
        ]
}

rules2 = {
        "rounding_rules": [
            {"max": 10, "endings": [0.90, 0.50]},
            {"min": 10, "max": 500, "endings": [0.90, 0.50]},
            {"min": 500, "endings": [20.00]}
        ]
}

assert advanced_round(rules1, 14.67) == 14.00, "using rules1, this is rounded down to nearest 5"
assert advanced_round(rules2, 17.70) == 17.90, "using rules 2, this should be rounded up to 17.90"
assert advanced_round(rules1, 1000) == 1010


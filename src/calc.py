def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    """Integer-safe division. Raises ZeroDivisionError on b == 0."""
    return a / b

def mean(values):
    if not values:
        return 0
    return sum(values) / len(values)

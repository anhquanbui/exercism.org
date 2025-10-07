def steps(number: int) -> int:
    """Return the number of steps required to reach 1 in the Collatz sequence."""
    
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    steps = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        steps += 1

    return steps

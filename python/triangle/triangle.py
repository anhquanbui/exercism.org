def equilateral(sides):
    """
    Return True if the triangle defined by `sides` is equilateral.

    Parameters
    ----------
    sides : iterable of 3 numbers
        The three side lengths (e.g., list/tuple). Each must be > 0.

    Rules / Expectations
    --------------------
    - Validate input length == 3.
    - Reject nonpositive sides (<= 0) -> not a valid triangle.
    - Enforce triangle inequality with strict '>' (a + b > c).
      If any sum equals the remaining side, it's degenerate -> False.
    - Equilateral: all three sides are equal (within a small tolerance for floats).

    Notes
    -----
    - Use a small epsilon (e.g., 1e-9) when comparing floats to handle tiny errors.
    - This function should NOT mutate the incoming list/tuple.
    """
    a, b, c = sides
    return _valid_triangle(a, b, c) and a == b == c


def isosceles(sides):
    """
    Return True if the triangle defined by `sides` is isosceles.

    Parameters
    ----------
    sides : iterable of 3 numbers
        The three side lengths (e.g., list/tuple). Each must be > 0.

    Rules / Expectations
    --------------------
    - Validate there are exactly 3 positive sides.
    - Enforce the strict triangle inequality (no degenerate triangles).
    - Isosceles: at least two sides are equal (within tolerance).
      *Note:* By most definitions, an equilateral triangle is also isosceles
      because it has at least two equal sides. If your assignment excludes
      equilateral from isosceles, add an extra check to return False for
      the all-equal case.

    Notes
    -----
    - Use a float tolerance (epsilon) for equality comparisons.
    - Consider normalizing order: sort the sides before inequality checks.
    """
    a, b, c = sides
    if not _valid_triangle(a, b, c):
        return False
    at_least_two_equal = (a == b) or (b == c) or (a == c)
    if include_equilateral:
        return at_least_two_equal
    # exclude the all-equal case
    return at_least_two_equal and not (a == b == c)


def scalene(sides):
    """
    Return True if the triangle defined by `sides` is scalene.

    Parameters
    ----------
    sides : iterable of 3 numbers
        The three side lengths (e.g., list/tuple). Each must be > 0.

    Rules / Expectations
    --------------------
    - Validate input (3 positive numbers).
    - Enforce strict triangle inequality (no degenerate triangles).
    - Scalene: all three sides are different (no pair equal within tolerance).

    Notes
    -----
    - Use a small epsilon for float comparisons.
    - If any pair is effectively equal (|a-b| <= eps), it's NOT scalene.
    """
    a, b, c = sides
    return _valid_triangle(a, b, c) and (a != b) and (b != c) and (a != c)

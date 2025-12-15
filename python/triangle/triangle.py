# triangle.py

from typing import Iterable

_EPS = 1e-12  # tolerance for float comparisons

def _valid_triangle(a: float, b: float, c: float) -> bool:
    """All sides > 0 and strict triangle inequality (non-degenerate)."""
    if min(a, b, c) <= 0:
        return False
    a, b, c = sorted((a, b, c))
    # strict: a + b > c (allow tiny float noise)
    return (a + b) > (c + _EPS)

def _eq(x: float, y: float) -> bool:
    return abs(x - y) <= _EPS

def equilateral(sides: Iterable[float]) -> bool:
    a, b, c = map(float, sides)
    return _valid_triangle(a, b, c) and _eq(a, b) and _eq(b, c)

def isosceles(sides: Iterable[float]) -> bool:
    # Exercism expects equilateral to be considered isosceles
    a, b, c = map(float, sides)
    if not _valid_triangle(a, b, c):
        return False
    return _eq(a, b) or _eq(b, c) or _eq(a, c)

def scalene(sides: Iterable[float]) -> bool:
    a, b, c = map(float, sides)
    if not _valid_triangle(a, b, c):
        return False
    return (not _eq(a, b)) and (not _eq(b, c)) and (not _eq(a, c))
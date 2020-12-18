"""
This module implements a number of iterator building blocks.
"""

def combinations(iterable, r):
    """(iterable, int) -> generator

    Return r length subsequences of elements from the input iterable.

    >>> list(combinations('ABC', 2))
    [('A', 'B'), ('A', 'C'), ('B', 'C')]
    >>> list(combinations(range(4), 3))
    [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    >>> list(combinations([], 3))
    []
    >>> list(combinations('ABC', 0))
    [()]
    >>> list(combinations('ABC', 6))
    []
    """
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

"""
This module implements a number of iterator building blocks.
"""

def count(start=0, step=1):
    '''
    Return infinite iterator through evenly spaced numbers
    starting with start
    >>> next(count())
    0
    >>> gen = count(2, 2); [next(gen) for _ in range(5)]
    [2, 4, 6, 8, 10]
    >>> gen = count(2, -1); [next(gen) for _ in range(5)]
    [2, 1, 0, -1, -2]
    >>> gen = count(0, 0); [next(gen) for _ in range(5)]
    [0, 0, 0, 0, 0]
    '''
    num = start
    while True:
        yield num
        num += step


def cycle(iterable):
    '''
    Return infinite iterator through iterable
    >>> cyc = cycle('ABC'); [next(cyc) for _ in range(5)]
    ['A', 'B', 'C', 'A', 'B']
    >>> cyc = cycle([7, 8, 9]); [next(cyc) for _ in range(5)]
    [7, 8, 9, 7, 8]
    >>> cyc = cycle([1]); [next(cyc) for _ in range(5)]
    [1, 1, 1, 1, 1]
    '''
    while iterable:
        for el in iterable:
            yield el


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


def combinations_with_replacement(r:int, n:int, human_count=False) -> list:
    '''
    Returns generator of combinations C(r, n) with repetitions in sorted order
    r - elements in each combination
    n - total length of possible values for each position
    human_count - if True counting starts from 1, else from 0

    * Steps indicates the step number accordingly to the proposed human language algorithm
    in lecture

    >>> list(combinations_with_replacement(0, 0))
    []
    >>> list(combinations_with_replacement(2, 4, True))
    [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
    >>> list(combinations_with_replacement(2, 4, False))
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
    >>> list(combinations_with_replacement(2, 1))
    [(0, 0)]
    >>> list(combinations_with_replacement(2, 2))
    [(0, 0), (0, 1), (1, 1)]
    '''

    if n == 0 or r == 0:
        return []
    nums = list(range(1, n+1) if human_count else range(n))

    rec_combo = [nums[0] for _ in range(r)]
    yield tuple(rec_combo)

    while True:
        # step 1
        for i in range(len(rec_combo)-1, -1, -1):
            if rec_combo[i]+1 in nums:

                # step 2
                rec_combo[i] += 1

                yield tuple(rec_combo)
                break

            if i == 0: return

            if not rec_combo[i-1] + 1 in nums:
                continue

            # step 3
            rec_combo[i-1:] = [rec_combo[i-1]+1]*(len(rec_combo)-i+1)

            yield tuple(rec_combo)

            break

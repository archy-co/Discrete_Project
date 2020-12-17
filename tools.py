'''Some iter tools'''


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
    i = 0
    length = len(iterable)
    while True:
        yield iterable[i]
        i = (i + 1) % length


if __name__ == '__main__':
    import doctest
    doctest.testmod()

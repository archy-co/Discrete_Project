from tools import count, cycle
import itertools
import pytest

def test_counter():
    params = ((0, 2), (-1, 0), (1.1, 9))
    for i in params:
        my_counter = count(*i)
        of_counter = itertools.count(*i)
        for _ in range(10):
            assert next(my_counter) == next(of_counter)


def test_cycle():
    params = (['a', 'b'], [0], 'ABC', 'A', )
    for i in params:
        my_cycler = cycle(i)
        of_cycler = itertools.cycle(i)
        for _ in range(10):
            assert next(my_cycler) == next(of_cycler)

def test_cycle_exception():
    my_cycler = cycle([])
    with pytest.raises(StopIteration):
        next(my_cycler)

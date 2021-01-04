"""
A testing module for itertools.py
"""

import itertools
import pytest
import tools

def test_counter():
    params = ((0, 2), (-1, 0), (1.1, 9))
    for i in params:
        my_counter = tools.count(*i)
        of_counter = itertools.count(*i)
        for _ in range(10):
            assert next(my_counter) == next(of_counter)


def test_cycle():
    params = (['a', 'b'], [0], 'ABC', 'A', )
    for i in params:
        my_cycler = tools.cycle(i)
        of_cycler = itertools.cycle(i)
        for _ in range(10):
            assert next(my_cycler) == next(of_cycler)


def test_cycle_exception():
    my_cycler = tools.cycle([])
    with pytest.raises(StopIteration):
        next(my_cycler)


def test_combinations():
    """
    Test tools.combinations.
    """
    # testing different iterable types
    assert list(tools.combinations('ABC', 2)) == (
        list(itertools.combinations('ABC', 2))
    )

    assert list(tools.combinations(['A', 'B', 'C'], 2)) == (
        list(itertools.combinations(['A', 'B', 'C'], 2))
    )

    assert list(tools.combinations(('A', 'B', 'C'), 2)) == (
        list(itertools.combinations(('A', 'B', 'C'), 2))
    )

    assert list(tools.combinations({'A', 'B', 'C'}, 2)) == (
        list(itertools.combinations({'A', 'B', 'C'}, 2))
    )

    assert list(tools.combinations(frozenset({'A', 'B', 'C'}), 2)) == (
        list(itertools.combinations(frozenset({'A', 'B', 'C'}), 2))
    )

    assert list(tools.combinations({'A': 1, 'B': 2, 'C': 3}, 2)) == (
        list(itertools.combinations({'A': 1, 'B': 2, 'C': 3}, 2))
    )

    # testing r == 0
    assert list(tools.combinations('ABC', 0)) == (
        list(itertools.combinations('ABC', 0))
    )

    # testing an empty iterable
    assert list(tools.combinations('', 2)) == (
        list(itertools.combinations('', 2))
    )

    # testing r == 0 and an empty iterable
    assert list(tools.combinations('', 0)) == (
        list(itertools.combinations('', 0))
    )


# combinations_with_replacement
def test_comb_with_rep_bc():
    '''
    Test combinations_with_replacement for some basic arguments in comparison
    with original itertools module function implementation
    '''

    params = ((3, 0), (2, 1), (2, 2), (3, 2))
    for r, n in params:
        my_result = tools.combinations_with_replacement(r, n)
        original = itertools.combinations_with_replacement(range(n), r)
        assert list(my_result) == list(original)


def test_comb_with_rep_zero_value_1():
    assert list(tools.combinations_with_replacement(0, 5)) == []


def test_comb_with_rep_human_count_1():
    assert list(tools.combinations_with_replacement(2, 4, True)) == [
        (1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]


def test_comb_with_rep_human_count_2():
    assert list(tools.combinations_with_replacement(2, 4, False)) == [
        (0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

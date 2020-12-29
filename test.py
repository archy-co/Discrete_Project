"""
A testing module for itertools.py
"""

import itertools

# testing different iterable types
def test_combinations_1():
    assert list(itertools.combinations('ABC', 2)) == [
        ('A', 'B'), ('A', 'C'), ('B', 'C')]


def test_combinations_2():
    assert list(itertools.combinations(['A', 'B', 'C'], 2)) == [
        ('A', 'B'), ('A', 'C'), ('B', 'C')]


def test_combinations_3():
    assert list(itertools.combinations(('A', 'B', 'C'), 2)) == [
        ('A', 'B'), ('A', 'C'), ('B', 'C')]


def test_combinations_4():
    assert list(itertools.combinations({'A', 'B', 'C'}, 2)) == [
        ('B', 'A'), ('B', 'C'), ('A', 'C')]


def test_combinations_5():
    assert list(itertools.combinations(frozenset({'A', 'B', 'C'}), 2)) == [
        ('B', 'A'), ('B', 'C'), ('A', 'C')]


def test_combinations_6():
    assert list(itertools.combinations({'A': 1, 'B': 2, 'C': 3}, 2)) == [
        ('A', 'B'), ('A', 'C'), ('B', 'C')]


# testing r == 0
def test_combinations_7():
    assert list(itertools.combinations('ABC', 0)) == [()]


# testing an empty iterable
def test_combinations_8():
    assert list(itertools.combinations('', 2)) == []


# testing r == 0 and an empty iterable
def test_combinations_9():
    assert list(itertools.combinations('', 0)) == [()]

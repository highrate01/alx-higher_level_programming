#!/usr/bin/python3
"""
find peak in the list of int
"""

def find_peak(list_of_integers):
    """
    finds a peak int the list of unsorted integers
    Args:
        list_of_integers(list): reps a list of integers
        to find peak from
    returns:
        int
    """
    if not list_of_integers:
        return None
    length = len(list_of_integers)

    start, end = 0, length - 1

    while start < end:
        mid = start + (end - start) // 2

        _list = list_of_integers

        if _list[mid] > _list[mid - 1] and _list[
                mid] > _list[mid + 1]:
            return _list[mid]
        elif _list[mid - 1] > _list[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return _list[start]

#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or all(weight == 0 for _, weight in my_list):
        return 0

    num = 0
    den = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]

    return (num / den)

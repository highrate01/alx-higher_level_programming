#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied_dict = {key: val * 2 for key, val in a_dictionary.items()}
    return multiplied_dict

#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ''
    i = 0
    for char in str:
        if i != n:
            new_string += str[i]
        i += 1
    return (new_string)

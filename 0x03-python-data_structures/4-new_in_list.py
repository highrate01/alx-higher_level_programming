#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
       #updated_list = my_list[:]
        my_list[idx] = element
        #return updated_list
    return my_list

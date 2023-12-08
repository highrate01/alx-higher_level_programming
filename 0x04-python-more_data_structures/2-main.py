#!/usr/bin/python3
#uniq_add = __import__('2-uniq_add').uniq_add
import importlib
import_module = '2-uniq_add'
uniq_add_module = importlib.import_module(import_module)
uniq_add = uniq_add_module.uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

#!/usr/bin/python3
import importlib
#common_elements_module = __import__('3-common_elements').common_elements
common_elements_module = importlib.import_module('3-common_elements')
common_elements = common_elements_module.common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

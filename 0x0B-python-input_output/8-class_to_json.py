#!/usr/bin/python3
"""Defines a python class-to-json function"""


def class_to_json(obj):
    """REturns the dictionary reps of a simple data struct"""
    return obj.__dict__

#!/usr/bin/python3
"""Defines a class myint that inherit from int."""


class MyInt(int):
    """invert int operations == !=."""

    def __eq__(self, value):
        """overrides == operator with != behaviour."""
        return self.real != value

    def __ne__(self, value):
        """overrides != operator with == bahaiour."""
        return self.real == value

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -(last_digit)
    thestring = "Last digit of {} is {}".format(number, last_digit)
if last_digit > 5:
    print(f"{thestring} and is greater than 5")
elif last_digit == 0:
    print(f"{thestring} and is 0")
elif last_digit < 6:
    print(f"{thestring} and is lass than 6 and not 0")

#!/usr/bin/python3
def arg_line(av):
    number = len(av) - 1
    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(number))
    i = 1
    while i <= number:
        print("{:d}: {}".format(i, av[i]))
        i += 1

if __name__ == "__main__":
    import sys
    arg_line(sys.argv)

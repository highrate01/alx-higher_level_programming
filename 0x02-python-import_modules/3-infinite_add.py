#!/usr/bin/python3
def add_args(argv):
    number = len (argv) - 1
    if number == 0:
        print("{:d}".format(number))
        return
    else:
        i = 1
        add = 0
        while i <= number:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))

if __name__ == "__main__":
    import sys
    add_args(sys.argv)

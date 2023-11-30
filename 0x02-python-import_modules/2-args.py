#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_line = sys.argv
    line_size = len(arg_line) - 1

    if line_size == 0:
        print("{} arguments".format(line_size))
    elif line_size > 1:
        print("{} arguments:".format(line_size))
        for i in range(1, line_size + 1):
            print("{}: {}".format(i, arg_line[i]))
    else:
        print("{} argument:".format(line_size))
        print("{}: {}".format(1, arg_line[1]))

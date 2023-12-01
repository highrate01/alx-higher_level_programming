#!usr/bin/python3
def no_c(my_string):
    new_chr = ""

    for i in my_string:
        if (i != 'c') and (i != 'C'):
            new_chr += i
    return(new_chr)

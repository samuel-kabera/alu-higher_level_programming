#!/usr/bin/python3
def no_c(my_string):
    tmp = list(my_string)
    count = len(tmp)
    new_string = ""
    for i in range(0, count):
        if tmp[i] != "c" and tmp[i] != "C":
            new_string += tmp[i]
    return new_string

#!/usr/bin/python3
def no_c(my_string):
    ret = ""
    for i in range(len(my_string)):
        if 'c' in my_string or 'C' in my_string:
            continue
        else:
            ret += my_string[i]
        return ret

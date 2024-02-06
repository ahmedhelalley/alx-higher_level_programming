#!/usr/bin/python3
'''Description Module for MyList class.'''


class MyList(list):
    '''Custom MyList class.'''
    def print_sorted(self):
        '''Method for printing a sorted list.'''
        print(sorted(self))

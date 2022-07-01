#!/usr/bin/python3

'''
Given n number of characters and return minimum number of operations
'''


def minoperations(n):
    '''
    return minimum operations to get n number of Hs
    '''
    operations = 0
    index = 2
    if n < 2:
        return 0
    while index < n + 1:
        while n % index == 0:
            operations += index
            n = n / index
        index += 1
    return operations

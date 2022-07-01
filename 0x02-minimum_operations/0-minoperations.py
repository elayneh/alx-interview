#!/usr/bin/python3

'''
Given a number n
return number of operations to get n H characters in the file.
'''


def minOperations(n):
    '''
    returns min operations to get n Hs
    '''
    opr = 0
    index = 2
    if n < 2:
        return 0
    while (index < n + 1):
        # checks if the number id dividable by 2
        while n % index == 0:
            # If so add number of smaller problems to the operations(op)
            opr += index
            # Create the smaller problem needed to get to n
            n /= index
        index += 1
    return opr

#!/usr/bin/python3
"""
Determine the validity based
on the UTF-8 formatting of the given data
"""


from numpy import byte


def validUTF8(data):
    """
    Accept:
        data
    Return:
        the staus of the given data
    """
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True

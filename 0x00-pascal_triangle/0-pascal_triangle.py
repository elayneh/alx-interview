#!/usr/bin/python3

def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return triangle
    prev = [1]
    for row in range(n):
        rlist = []
        if row == 0:
            rlist = [1]
        else:
            for index in range(row + 1):
                if index == 0:
                    rlist.append(0 + prev[index])
                elif index == row:
                    rlist.append(prev[index - 1] + 0)
                else:
                    rlist.append(prev[index - 1] + prev[index])
        prev = rlist
        triangle.append(rlist)
    return triangle

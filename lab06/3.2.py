__author__ = 'student'
import numpy as np


def get_percentile_number(value, percentiles):
    k = 0
    if value <= percentiles[0]:
        k = 0
    elif value >= percentiles[len(percentiles)-1]:
        k = len(percentiles)
    else:
        for i in range(len(percentiles) - 1, 0, -1):
            if percentiles[i] <= value:
                k = i
                break

    return k


def get_percentile(values, n):
    k = 100 / n
    a = 0
    t = []
    while a != 100:
        t.append(np.percentile(values,a))
        a += k
    if min (values) >= 0:
        t[0] = 0.0
    return t

#def  value_equalization(value, percentiles):


l = []
values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
n = int (input())
l = get_percentile(values, n)
print(' '.join(map(str, l)))
a = int(input())
print(get_percentile_number(a, l))
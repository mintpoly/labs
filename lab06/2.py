__author__ = 'student'
import random
n = int(input())
def integral(a):
    if a > -2 and a < 2:
        return -a ** 2 +4
    else:
        return 0
values = [random.uniform(-3,3) for i in range (n)]
s = 0
for i in range (n):
    s += integral(values[i])
print(6 / n * s)
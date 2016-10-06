__author__ = 'student'
import random
import matplotlib.pyplot as plt

random.seed()
n = 100
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)
plt.show()
n = 1000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)
plt.show()
n = 10000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)
plt.show()
n = 100000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)
plt.show()

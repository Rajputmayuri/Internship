"""1st way"""

n = 20
factors = []
for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)
print("factors:", factors)

"""2nd way"""

n = 20
factors = []
for i in range(1, n // 2 + 1):
    if n % i == 0:
        factors.append(i)
factors.append(n)
print("factors:", factors)


"""3rd way"""
from math import sqrt
from typing import List

n = 20
result = []
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        result.append(i)
    if n // i != i:
        result.append(n // i)
factors.sort()
print("factors :", factors)

"""Q) Input: 'X' = 2

Output: 1

As only one digit is ‘2’ present in ‘X’ so answer is ‘1’."""


def countdigit():
    n = "127868763"
    count = 0
    for i in n:
        count += 1
    print(count)


countdigit()

"""Using logarithmic method"""

from math import log10


def countdigit(n):
    if n == 0:
        return 1
    return int(log10(abs(n))) + 1


num = 12345678
result = countdigit(num)
print("Number of digits :", result)

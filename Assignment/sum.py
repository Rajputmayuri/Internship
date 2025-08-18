# 2. Find sum of digits (245 → 11)


def getsum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = 245
print(getsum(n))

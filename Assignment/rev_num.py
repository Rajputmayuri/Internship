# 1. Reverse a number (e.g., 123 → 321)

num = 123
s = str(num)
reversed_s = s[::-1]
print(reversed_s)

#using for loop

num = 123
s = str(num)
for digit in s:
    reversed_s = s[::-1]
print(reversed_s)



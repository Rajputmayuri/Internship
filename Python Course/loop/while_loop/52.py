"""Q52. Calculate how many numbers are divisible by 6 and 7
between 1 to 200"""

count = 0
i = 1
while i <= 200:
    if i % 6 == 0 and i % 7 == 0:
        count += 1
    i += 1
print("The numbers that are divisible by 6 & 7 between 1 to 200 are=",count)

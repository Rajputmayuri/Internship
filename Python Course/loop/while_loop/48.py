"""Q48. Calculate how many numbers are divisible by both
6 and 7 between 1 to 200"""

i = 1
count = 0
while i <= 200:
    if i % 6 == 0 and i % 7 == 0:
        print(i, end=" ")
        count += 1
    i = i+1
print("The numbers divisible by 6 and 7 are =", count)

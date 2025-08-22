"""Q47. Calculate how many numbers are divisible by 
7 from 1 to 100"""

count = 0
i = 1
while i <= 100:
    if i % 7 == 0:
        print(i, end=" ")
        count += 1
    i = i+1
print()
print("The numbers divisible by 7 from 1 to 100 are=", count)

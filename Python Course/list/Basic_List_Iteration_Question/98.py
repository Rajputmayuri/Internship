"""Q98. Count how many numbers are divisible by both
2 and 5 in that list."""

my_list = [51, 85, 91.66, 52, 44, 100, 200]
count = 0

for i in my_list:
    if i % 2 == 0 and i % 5 == 0:
        count += 1
print(count)

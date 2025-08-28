"""Q99. Find the sum of all even numbers present
in that list."""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in my_list:
    if i % 2 == 0:
        sum += i
print(sum)

"""Q102. Print the largest number in that list."""

my_list = [1, 65, 90, 43, 54, 75, 100]
"""large = max(my_list)
print(large)"""


large = my_list[0]

for num in my_list:
    if num > large:
        large = num
print(large)

"""Q103. Print the smallest number in that list."""

my_list = [1, 2, 3, 4, 5]
"""small = min(my_list)
print(small)
"""

small = my_list[0]
for i in my_list:
    if i < small:
        small = i
print(small)

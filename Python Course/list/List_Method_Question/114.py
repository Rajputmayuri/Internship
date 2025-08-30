"""Q114. Write a Python code to find the occurrence of each element in a list
and print the element with the highest occurrence."""

my_list = [12, 43, 65, 12, 87, 34, 12]
max_count = 0

for i in my_list:
    count = my_list.count(i)
    if count > max_count:
        max_count = count
print(f"count of {i} in list :", max_count)

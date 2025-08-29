"""Q109. Start by creating two separate lists with random numbers. Then,
create a third list that merges the numbers from the first and second lists
together."""

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
merged_list = []

for i in list1:
    merged_list.append(i)
for i in list2:
    merged_list.append(i)
print("Merged list=", merged_list)

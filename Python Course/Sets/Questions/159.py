"""Q159. Python program to find common elements in
three lists using sets."""

list1 = [5, 4, 3, 2, 1]
list2 = [1, 2, 8, 9, 5]
list3 = [9, 4, 1, 5, 8]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

output = set1.intersection(set2)
output1 = output.intersection(set3)
print(output1)

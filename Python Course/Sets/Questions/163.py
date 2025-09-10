"""Q163. Write a python program to check if two given
sets have no elements in common."""

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

result = set1.intersection(set2)

if len(result) == 0:
    print("No common elements are found in sets..")
else:
    print("Sets have common elements :", result)

# using isdisjoint method
result = set1.isdisjoint(set2)
print(result)

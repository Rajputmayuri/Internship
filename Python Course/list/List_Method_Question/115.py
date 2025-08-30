"""Q115. Write a program that has two lists
and make a new list that contains
only the common elements between them without duplicates.
"""
list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 4, 5, 6, 7]
output = []

for i in list1:
    if i in list2:
        if i not in output:
            output.append(i)
print(output)

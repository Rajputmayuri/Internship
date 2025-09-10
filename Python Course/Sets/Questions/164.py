"""Q164. Write a python program to find elements in
a given set that are not in anohther set."""

set1 = {1, 2, 3, 4, 5, 6}
set2 = {8, 9, 1, 3}

print(set2.difference(set1))
# the difference method in set is used to find the unique element from one set that are not in another set.

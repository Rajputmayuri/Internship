my_set1 = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 5, 6, 7}

# Union and Intersection
print(my_set1.union(my_set2))
print(my_set1.intersection(my_set2))

# to create a empty set
my_set = set()
print(type(my_set))

# to add the element in the set
my_set.add(100)
my_set.add(200)
my_set.add(300)
print(my_set)

# to remove the element from set

my_set.remove(200)
print(my_set)

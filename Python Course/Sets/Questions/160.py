"""Q160. Create 3 sets of your own, find the union
of three sets."""

set1 = {1, 2, 3, 4, "mayuri", "rajput"}
set2 = {90, 45, 23, 1, 4, "rajput"}
set3 = {12, 65, 9, 45, "gayatri"}

output = set1.union(set2)
output1 = output.union(set3)
print(output1)

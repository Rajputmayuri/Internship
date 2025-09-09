"""Q144. Write a python program to sum all the items
in a dictionary."""

sub_marks = {"math": 60, "sciecne": 90, "english": 80, "biology": 50}

total = 0
for i in sub_marks.values():
    total += i
print(total)

# print(sum(list(sub_marks.values())))

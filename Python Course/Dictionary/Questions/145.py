"""Q145. Write a python program to multiply all the
items in a dictionary."""

sub_marks = {"math": 60, "sciecne": 90, "english": 80, "biology": 50}

prod = 1
for i in sub_marks.values():
    prod *= i
print(prod)

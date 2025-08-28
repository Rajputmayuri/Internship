"""Q95. Print all the elements present at even index position."""

my_list = [89, 76, 12, 54, 9.87, -9, "mayuri"]
a = len(my_list)

for i in range(0, a):
    if (i % 2 == 0):
        print(my_list[i], end=" ")
print()

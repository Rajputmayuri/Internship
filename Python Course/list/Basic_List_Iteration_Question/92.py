"""Q92. Print the list in reverse."""

my_list = [89, 76, 12, 54, 9.87, -9, "mayuri"]
print(my_list[::-1])

# using for loop

for i in range(len(my_list)-1, -1, -1):
    print(my_list[i], end=" ")

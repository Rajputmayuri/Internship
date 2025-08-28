"""Q93.Print all the even numbers present in the list."""

# Iteration by value
my_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in my_list:
    if i % 2 == 0:
        print(i, end=" ")

# Iteration by index
for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        print(my_list[i], end=" ")

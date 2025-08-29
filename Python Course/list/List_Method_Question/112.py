"""Q112. Take 10 integer inputs from user and store them in a list. Now, copy
all the elements in another list but in reverse order."""

my_list = []
for i in range(0, 10):
    num = int(input(f"Enter a {i} number="))
    my_list.append(num)
print(my_list)

reversed_list = my_list.copy()
reversed_list.reverse()
print(reversed_list)

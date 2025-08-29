"""Q111.Make a list. Then ask a number from user.
if number exists in that list then print position
of the element else print -1"""

my_list = [1, 3, 6, 9, 23, 90, 16, 45]
print(my_list)
num = int(input("Enter value="))

if num in my_list:
    index_position = my_list.index(num)
    print(f"The position of {num} is :", index_position)
else:
    print("-1")

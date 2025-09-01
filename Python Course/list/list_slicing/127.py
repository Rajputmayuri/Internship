"""Q127. Implement a python program to split a list into two equal parts using
slicing. One list should contain 1st half and another list should contain 2nd
half."""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = len(my_list)//2
list1 = my_list[:a]
print(list1)
list2 = my_list[a:]
print(list2)

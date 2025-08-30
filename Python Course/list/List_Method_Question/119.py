"""Q119. Write a program to split a given list 
into two halves."""

my_list = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
half = len(my_list) // 2
list1 = []
list2 = []

for i in range(half):
    list1.append(my_list[i])

for i in range(half, len(my_list)):
    list2.append(my_list[i])

print("list1", list1)
print("list2", list2)

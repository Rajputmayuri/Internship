"""Q128. Implement a python program to get the last
'n' elements from a list using slicing."""


my_list = [12, 43, 76, 23, 90, 76, 34, 87]
num = int(input("Enter n="))
output = my_list[-num:]
print(output)

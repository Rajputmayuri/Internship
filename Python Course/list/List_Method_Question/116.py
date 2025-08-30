"""Q116. Write a Python code to find the second largest element in a list
without sorting."""

# my_list.sort()
# print(my_list)
# print(my_list[-2])

"""Without sorting"""
my_list = [10, 20, 9, 65, 100]
largest = float("-inf")
second_largeset = float("-inf")

for num in my_list:
    if num > largest:
        second_largeset = largest
        largest = num
    elif num > second_largeset and num < largest:
        second_largeset = num

print("second largest element in list=", second_largeset)

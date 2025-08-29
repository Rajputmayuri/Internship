"""Q113. Write a program to find the average of all the numbers present in the
list."""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 0
for i in my_list:
    a += i
print("Total of numbers=", a)
average = a/len(my_list)
print("Average=", average)

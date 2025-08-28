"""Q97.Count the number of even numbers present in list"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = len(my_list)
count = 0
for i in range(0, a):
    if i % 2 == 0:
        count += 1
print("Count of even number in list is=", count)

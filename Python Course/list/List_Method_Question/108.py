"""Q108. Generate a list of at least 10 numbers. Then, create two separate
lists called 'odd' and 'even.' Put all the odd numbers from the original list
into the 'odd' list, and all the even numbers into the 'even' list."""

my_list = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
odd = []
even = []

for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        even.append(my_list[i])
    else:
        odd.append(my_list[i])
print("odd=", odd)
print("even=", even)

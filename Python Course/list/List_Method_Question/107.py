"""Q107.Ask the user for a number. Then, from a list of numbers, remove all
the numbers that can be divided by the number the user entered. """

my_list = [12, 14, 10, 15, 60, 40, 68, 50]
num = int(input("Enter a number="))
output = []

for i in range(0, len(my_list)):
    if my_list[i] % num != 0:
        output.append(my_list[i])
print(output)

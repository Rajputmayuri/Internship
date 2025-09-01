"""Q129. Ask ‘n’ from user. Create a list of last n elements but in reverse order
using slicing."""

my_list = [12, 43, 76, 23, 90, 76, 34, 87]
num = int(input("Enter n="))
output = my_list[:-num-1:-1]
print(output)

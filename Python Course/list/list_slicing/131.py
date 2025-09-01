"""Q131. Ask ‘n’ from user. Create a list of first n elements but in reverse order
using slicing."""

my_list = [12, 95, 74, 32, 14, 96, 85, 14]
n = int(input("Enter n="))
output = my_list[0:n]
reversed_output = output[::-1]
print(reversed_output)

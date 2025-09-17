n = 153
num = n
output = 0
number_of_digit = len(str(num))

while num > 0:
    last_digit = num % 10
    output = output + last_digit**number_of_digit
    num //= 10
print(n == output)

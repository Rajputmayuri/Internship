"""Q50. Ask a number from user. print the multiplication
table of that number """

num = int(input("Enter a number="))
i = 1
while i < 11:
    product = num*i
    print(num, "x", i, "=", product)
    i = i+1

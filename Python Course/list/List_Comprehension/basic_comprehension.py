"""Even  Odd"""
# my_list = ["EVEN" if i % 2 == 0 else "ODD" for i in range(1, 21)]
# print(my_list)


"""even odd number"""
# my_list = [i for i in range(1, 31) if i % 2 == 0]
# print(my_list)

"""ask start and end number from user and print
the numbers that are divisible by 2 & 3"""

start = int(input("Enter start number="))
end = int(input("Enter end number="))
my_list = [i for i in range(start, end) if i % 2 == 0 and i % 3 == 0]
print(my_list)

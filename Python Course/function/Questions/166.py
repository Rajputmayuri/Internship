"""Q166. Write a function that accepts an integer and
prints the multiplication table for that number up
to 10"""


def mul_table():
    num = int(input("Enter a number="))
    for i in range(1, 11):
        prod = num * i
        print(f"{num} X {i} = {prod}")


mul_table()

"""Q170. Write a function that takes a list of num
bers and prints the sum and average of these numbers."""


def number():
    total = 0
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in list1:
        total += i
        average = total / 10
    print("total :", total)
    print("average :", average)


number()

"""Basic Calculator – Create a program that performs addition, subtraction, multiplication, and division based on user input."""


def cal():
    num1 = int(input("Enter a 1st number= "))

    print("\n Which operation you want to perform : ")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")

    operation = input("Enter which operation you want to perfomr = ")
    num2 = int(input("Enter a 2nd number= "))

    if operation == "1":
        print(f"Addition of {num1} and {num2} is :", num1 + num2)
    elif operation == "2":
        print(f"Subtraction of {num1} and {num2} is :", num1 - num2)
    elif operation == "3":
        print(f"Multiplication of {num1} and {num2} is :", num1 * num2)
    elif operation == "4":
        if num2 != 0:
            print(f"Division of {num1} and {num2} is :", num1 / num2)
        else:
            print("Division by 0 not allowed..")
    else:
        print("Invalid")


cal()

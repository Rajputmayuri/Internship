"""Q104. Write a program that promts the user to specify
the length of a list and then request numbers to 
populate that list. Display the final list as the
output"""

list_length = int(input("Enter the Length of the list="))
answer = []
for i in range(0, list_length):
    num = (int(input("Enter number=")))
    answer.append(num)
print(answer)

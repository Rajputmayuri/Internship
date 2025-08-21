"""Q34. A student will not be allowed to sit in exam if his/her attendance is
less than 75%.
a. Take following input from user
i. Number of classes held
ii. Number of classes attended.
b. Print percentage of class attended
c. Print Is student is allowed to sit in exam or not."""


class_held = int(input("Enter number of classes held="))
class_attended = int(input("Enter number of classes attended="))
percentage_of_class = ((class_attended/class_held)*100)
print("Percentage of class attended is", percentage_of_class)

if percentage_of_class >= 75:
    print("Student is allowed to sit in the exam")
else:
    print("Student is not allowed to sit in the exam because attendance is less thatn 75%")

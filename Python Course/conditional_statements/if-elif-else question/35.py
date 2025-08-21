""""Q35. Take Salary as input from User and Update the salary of an employee.
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment
"""

salary = int(input("Enter your salary="))
if salary < 10000:
    incre_salary1 = ((salary*5)/100)+salary
    print("Your salary will be incremented by 5%", incre_salary1)
elif salary >= 10000 and salary <= 20000:
    incre_salary2 = ((salary*10)/100)+salary
    print("Your salary will be incremented by 10%", incre_salary2)
elif salary >= 20000 and salary <= 50000:
    incre_salary3 = ((salary*15)/100)+salary
    print("Your salary will be incremented by 15%", incre_salary3)
elif salary >= 50000:
    incre_salary4 = ((salary*20)/100)+salary
    print("Your salary will be incremented by 20%", incre_salary4)

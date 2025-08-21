"""Q31. Write a program to calculate bill. Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid.
Example 1
Enter bill amount = 80000
You got 30% discount
Your final bill is Rs. 56000
"""

bill_amount = int(input("Enter bill amount="))
if bill_amount >= 50000:
    print("You got 30% discount")
    dis1 = bill_amount-(bill_amount*0.30)
    print("Your final bill is Rs.", dis1)
elif bill_amount >= 40000 and bill_amount <= 49999:
    print("You got 25% discount")
    dis2 = bill_amount-(bill_amount*0.25)
    print("Your final bill is Rs.", dis2)
elif bill_amount >= 30000 and bill_amount <= 39999:
    print("You got 20% discount")
    dis3 = bill_amount-(bill_amount*0.20)
    print("Your final bill is Rs.", dis3)
elif bill_amount >= 10000 and bill_amount <= 29999:
    print("You got 10% discount")
    dis4 = bill_amount-(bill_amount*0.10)
    print("Your final bill is Rs.", dis4)
else:
    print("No discount")

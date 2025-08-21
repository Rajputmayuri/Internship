"""Q40. Create a program that calculates the price of a movie ticket based on
the age of the customer. If the customer is under 12, the ticket costs $5; if
they are between 12 and 65, the ticket costs $10; otherwise, it's $7"""

age = int(input("Enter the age of customer="))
if age < 12:
    ticket_cost = "$5"
    print("Ticket cost is ", ticket_cost)
else:
    if age >= 12 and age <= 65:
        cost = "$10"
        print("Ticket cost is", cost)
    else:
        print("Ticket cost is $7")
 
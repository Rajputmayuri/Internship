"""Q14. Write a Python program to calculate the compound interest for a
given principal, rate of interest, and time period. Ask everything from the
user."""

principal_amount=int(input("Enter the princiapl amount="))
rate_of_interest=float(input("Enter the rate of interest="))
time_period=int(input("Enter the time period in years="))
interest=int(input("Enter the interest per year="))

compound_interest = principal_amount * \ (1+(rate_of_interest/interest))(interest_compounded_per_year*times_period)

print(f"Total compound Interest :{compound_interest}")
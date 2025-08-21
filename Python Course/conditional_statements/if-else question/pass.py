"""Ask physics and chemistry marks from user print
PASS, if student is passed in both subjects Else 
FAIL """

marks = 33
phy = int(input("Enter physics marks="))
chem = int(input("Enter chemistry marks="))
if (marks >= phy and marks >= chem):
    print("Student is PASS")
else:
    print("Student is FAIL")

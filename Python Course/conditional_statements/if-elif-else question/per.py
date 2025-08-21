"""Calculate percentage and print it
91-100 -> A grade
81-90 -> B grade
71-80 -> C grade
61-70 -> D grade
1-60 -> FAIL"""

math = int(input("Enter maths marks="))
science = int(input("Enter science marks="))
history = int(input("Enter history marks="))
english = int(input("Enter english marks="))
geography = int(input("Enter geography marks="))
total = math+science+history+english+geography
percentage = (total/500)*100
if percentage >= 91 and percentage <= 100:
    print("A grade")
elif percentage >= 81 and percentage <= 90:
    print("B grade")
elif percentage >= 71 and percentage <= 80:
    print("C grade")
elif percentage >= 61 and percentage <= 70:
    print("D grade")
elif percentage >= 1 and percentage <= 60:
    print("FAIL")
else:
    print("Invalid")

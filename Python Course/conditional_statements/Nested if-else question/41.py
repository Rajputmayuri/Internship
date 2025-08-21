"""Q41. Write a program that calculates a person's BMI based on their height
(in meters) and weight (in kilograms). Use the following formula: BMI =
weight / (height^2). Then, classify the BMI according to the following
ranges:
Underweight: BMI less than 18.5
Normal weight: BMI 18.5 - 24.9
Overweight: BMI 25 - 29.9
Obesity: BMI 30 or greater"""

height = float(input("Enter your height in meter="))
weight = int(input("Enter your weight="))
BMI = weight/(height**2)
print(BMI)
if BMI < 18.5:
    print(" underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal weight")
elif BMI >= 25 and BMI <= 29.9:
    print("Overwight")
else:
    print("Obesity")

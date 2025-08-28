"""Q101. Print how many positive and negative 
numbers."""

my_list = [12, 34, 54, -15, -76, 28, -76, 88, 65, 98]

positive = 0
negative = 0

for i in my_list:
    if i > 0:
        positive += 1
    else:
        negative += 1
print("Positive numbers in list=", positive)
print("Negative numbers in list=", negative)

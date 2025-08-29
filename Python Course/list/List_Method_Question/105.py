"""Q105. Create a list and prompt the user for an 
'old number' followed by a 'new number'. If the 
'old number' exists in this list, replace it with
the 'new number' provided by the user."""

my_list = [5, 10, 15, 20, 25, 30]
old_number = int(input("Enter the old number : "))
new_number = int(input("Enter the new number : "))

for num in range(0, len(my_list)):
    if old_number == my_list[num]:
        my_list[num] = new_number
print(my_list)

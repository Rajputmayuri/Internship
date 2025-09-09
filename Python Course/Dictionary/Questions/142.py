"""Q142. Ask subject name and marks from the user
and keep adding it to dictionary."""

my_dic = {}
sub = int(input("Enter the number of subject ="))
for i in range(0, sub):
    sub_name = input("Enter the subject name :")
    sub_marks = int(input(f"Enter the marks for {sub_name} :"))
    my_dic[sub_name] = sub_marks
    # my_dic.update({sub_name:sub_marks})
print(my_dic)

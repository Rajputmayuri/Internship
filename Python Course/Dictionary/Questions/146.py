"""Q146. Ask a string from user. Display the dictionary
where each key is a character and value is the
frequency of that character that comes in that string."""

my_dic = {}
a = input("Enter a string :")

for i in a:
    if i not in my_dic:
        my_dic[i] = 1
    else:
        my_dic[i] += 1
print(my_dic)

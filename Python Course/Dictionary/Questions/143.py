"""Q143. Convert two lists into a dictionary.
Make two list on your own of same length, and
convert them to dictionary."""

my_dic = {}
list1 = ["ten", "twenty", "thirty"]
list2 = [10, 20, 30]

for i in range(0, len(list1)):
    my_dic[list1[i]] = list2[i]
print(my_dic)

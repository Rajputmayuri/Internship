"""Q171.Write a function that accepts a string and
prints the frequency of each character in the string."""


def freq():
    my_string = input("Enter a string=")
    my_dic = {}

    for i in my_string:
        if i not in my_dic:
            my_dic[i] = 1
        else:
            my_dic[i] += 1
    print(my_dic)

    for k, v in my_dic.items():
        print(f"{k} occurs {v} times..")


freq()

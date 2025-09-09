my_dict={"name":"Mayuri",
         "age":15,
         "gender":"female"}

#using del
del my_dict["gender"]
print(my_dict)

#using pop
my_dict.pop("name")
print(my_dict)

my_dict.popitem()
print(my_dict)
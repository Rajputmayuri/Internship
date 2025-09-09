my_dict={"name":"Mayuri",
         "age":15,
         "gender":"female"}

print(my_dict)

#Method 1
my_dict["age"]=22
print(my_dict)

#Method 2 if key is not exist it add the new key 
my_dict["roll"]=12
print(my_dict)

#Method 3 multiple key value add using update
my_dict.update({"marks":99,"address":"chalisgaon"})
print(my_dict)
my_dict={
    "name":"mayuri",
    "age":21,
    "gender":"female"
}

#with the help of keys  iterating the dictionary
for k in my_dict.keys():
    print(k)

#with the helop of values iterating the dictionary
for k in my_dict.values():
    print(k)


for k,v in my_dict.items():
    print(f"{k} -> {v}")
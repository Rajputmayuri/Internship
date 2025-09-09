x={"name":"mayuri","age":15, "gender":"female"}
# to get a value
# r=y.get("gender")
# print(r)

k=input("Enter a key=")
result=x.get(k)

if result is not None:
    print(result)
else:
    print("Key does not exist")
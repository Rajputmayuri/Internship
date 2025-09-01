"""Q130. Ask start and end index from the user. Create a list from start index
to end index using slicing.
Q131. Ask ‘n’ from user. Create a list of first n elements but in reverse order
using slicing."""


a = [25, 62, 78, 96, 32, 10, 97, 69, 74]
start = int(input("Enter start index="))
end = int(input("Enter end index="))
output = a[start:end+1]
print(output)

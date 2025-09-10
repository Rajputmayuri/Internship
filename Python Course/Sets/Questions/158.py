"""Q158. Given two lists a,b. Check if two lists
have at least one element common in them."""

a = [1, 2, 3, 4, 5]
b = [1, 6, 7, 8, 2]

c = set(a)
d = set(b)

output = list(c.intersection(d))

print(output)

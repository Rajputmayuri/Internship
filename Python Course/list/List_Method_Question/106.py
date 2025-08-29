"""Q106. Remove all the even numbers from the list."""

a = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
b = []
for i in range(0, len(a)):
    if a[i] % 2 != 0:
        b.append(a[i])
print(b)

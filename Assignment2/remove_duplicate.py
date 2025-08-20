# 4. Remove duplicates from a list

list = [1, 2, 4, 1, 4, 5]
unique = []
duplicate = []
for i in list:
    if i not in duplicate:
        unique.append(i)
        duplicate.append(i)
print(unique)

"""Q110. Make a list of your own. And remove all the duplicates element from
that list."""

my_list = [1, 2, 4, 1, 5, 6, "mayuri", "mayuri"]
output = []

for i in my_list:
    if i not in output:
        output.append(i)
print(output)

"""Q124. Generate a list of list using list comprehension where format should
be [[1, ”ODD”], [2, “EVEN”], [3, ”ODD”]]."""

my_list = [f"[{i}, Even]" if i %
           2 == 0 else f"[{i}, Odd]" for i in range(1, 6)]
print(my_list)

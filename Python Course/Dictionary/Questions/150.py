"""Q150. Write a python program to combine two
dictionary by adding values for common keys."""

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
output = {}

for k, v in d1.items():
    output[k] = v

for k, v in d2.items():
    if k in output:
        output[k] = output[k] + v
    else:
        output[k] = v
print(output)

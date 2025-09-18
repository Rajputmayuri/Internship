"""1st Method"""

# num = [5, 4, 2, 7, 8, 1, 3, 2, 5, 9, 2]
# freq_map = {}
# for i in range(0, len(num)):
#     if num[i] in freq_map:
#         freq_map[num[i]] += 1
#     else:
#         freq_map[num[i]] = 1
# print(freq_map)

"""2nd Method"""
num = [5, 4, 2, 7, 8, 1, 3, 2, 5, 9, 2]
freq_map = {}
n = len(num)
for i in range(0, n):
    freq_map[num[i]] = freq_map.get(num[i], 0) + 1
print(freq_map)

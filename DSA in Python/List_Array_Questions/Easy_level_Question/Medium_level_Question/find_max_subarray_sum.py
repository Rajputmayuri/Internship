nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(nums)
maximum = float("-inf")
for i in range(0, n):
    total = 0
    for j in range(i, n):
        total = total + nums[j]
        maximum = max(maximum, total)
print(maximum)

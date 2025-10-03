"""Brute Force Solution"""

nums = [5, 10, -3, -1, -10, 6]
pos = []
neg = []
for i in nums:
    if i > 0:
        pos.append(i)
    elif i < 0:
        neg.append(i)
for i in range(0, len(pos)):
    nums[2 * i] = pos[i]
    nums[(2 * i) + 1] = neg[i]
print(nums)

"""Time Complexity :O(N+N/2)
    Space Complexity : O(N)"""

"""Optimal Solution"""
nums = [5, 10, -3, -1, -10, 6]
n = len(nums)
result = [0] * n
pos_index = 0
neg_index = 1
for i in range(0, n):
    if nums[i] >= 0:
        result[pos_index] = nums[i]
        pos_index += 2
    else:
        result[neg_index] = nums[i]
        neg_index += 2
print(result)

"""Time Complexity : O(N)
    Space Complexity : O(1)/O(N)"""

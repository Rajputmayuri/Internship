"""Bruteforce solution"""

nums = [9, 0, 3, 1, 2, 5, 6, 7, 4]
for i in range(0, len(nums)):
    if i not in nums:
        print(i)

"""Time Complexity : O(N^2)
    Space Complexity : O(1)"""

"""Better Solution"""
nums = [9, 0, 3, 1, 2, 5, 6, 7, 4]
freq = {i: 0 for i in range(0, len(nums) + 1)}
for i in nums:
    freq[i] += 1
for k, v in freq.items():
    if v == 0:
        print(k)

"""Time Complexity : O(3N)=O(N)
    Space Complexity : O(N)"""

"""Optimal Solution"""
nums = [9, 0, 3, 1, 2, 5, 6, 7, 4]
n = len(nums)
total = (n * (n + 1)) // 2
print(total - sum(nums))

"""Time Complexity : O(N)
    Space Complexity : O(1)"""

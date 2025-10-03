"""Brute Force Solution"""

nums = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]
max_count = 0
n = len(nums)
for i in range(0, n):
    num = nums[i]
    count = 1
    while num + 1 in nums:
        count += 1
        num = num + 1
    max_count = max(max_count, count)
print(max_count)

"""Time Complexity : O(N^2)
    Space Complexity : O(1)"""

"""Better Solution"""
nums = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]
nums.sort()
n = len(nums)
count = 0
last_smaller = float("-inf")
longest = 0
for i in nums:
    if i - 1 == last_smaller:
        count += 1
        last_smaller = i
    elif i != last_smaller:
        count = 1
        last_smaller = i
    longest = max(longest, count)
print(longest)

"""Time Complexity : O(NlogN+N)
    Space Complexity :O(1)"""

"""Optimal Solution"""
nums = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]
my_set = set()
n = len(nums)
for i in range(0, n):
    my_set.add(nums[i])
longest = 0
for num in my_set:
    if num - 1 not in my_set:
        x = num
        count = 1
        while x + 1 in my_set:
            count += 1
            x += 1
        longest = max(longest, count)
print(longest)

"""Time Complexity : O(N+N+N) = O(3N)
    Space Complexity : O(N)"""

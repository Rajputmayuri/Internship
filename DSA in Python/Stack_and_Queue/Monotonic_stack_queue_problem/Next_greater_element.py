# Brute force solution
nums = [19, 4, 2, 11, 6, 5, 3, 10]
n = len(nums)
ans = [-1] * n
for i in range(0, n):
    for j in range(i + 1, n):
        if nums[j] > nums[i]:
            ans[i] = nums[j]
            break
print(ans)

"""Time Complexity : O(N2)
Space Complexity : O(1)"""


# Optimal Solution

nums = [19, 4, 2, 11, 6, 5, 3, 10]
n = len(nums)
ans = [-1] * n
stack = []
for i in range(n - 1, -1, -1):
    while len(stack) != 0 and stack[-1] <= nums[i]:
        stack.pop()
    if len(stack) != 0:
        ans[i] = stack[-1]
    stack.append(nums[i])
print(ans)

"""TC : O(n)
    SC : O(n)"""

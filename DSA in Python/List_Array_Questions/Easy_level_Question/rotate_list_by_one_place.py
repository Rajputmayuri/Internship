"""Right Rotate Array by 1 place
nums=[1,4,5,6,2,5]
if we want to change the nums array then you should
use nums[:] it means the array is changed in same
address"""

"""with slicing"""
nums = [5, 2, 3, 9, 0, 6, 10, 7]
n = len(nums)
nums[:] = [nums[-1]] + nums[0 : n - 1]
print(nums)

"""without slicing"""
nums = [5, 2, 3, 9, 0, 6, 10, 7]
n = len(nums)
temp = nums[n - 1]
for i in range(n - 2, -1, -1):
    nums[i + 1] = nums[i]
nums[0] = temp
print(nums)

"""Time Complexity : O(N)
    Space Complexity : O(1)"""

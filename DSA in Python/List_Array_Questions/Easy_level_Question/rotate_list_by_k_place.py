"""1st method"""

nums = [8, 9, 3, 2, 1, 6, 7]
k = int(input("Enter value for k :"))
for _ in range(0, k):
    e = nums.pop()
    nums.insert(0, e)
print(nums)

"""2nd method"""
nums = [8, 9, 3, 2, 1, 6, 7]
n = len(nums)
k = int(input("Enter value for k :"))
rotations = k % n
for _ in range(0, rotations):
    e = nums.pop()
    nums.insert(0, e)
print(nums)

"""3rd method with help of slicing """

nums = [8, 9, 3, 2, 1, 6, 7]
n = len(nums)
k = int(input("Enter value for k :"))
rotations = k % n
nums[:] = nums[n - k :] + nums[: n - k]
print(nums)

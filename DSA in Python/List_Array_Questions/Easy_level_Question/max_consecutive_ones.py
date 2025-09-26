nums = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]
count = 0
max_count = 0
for i in nums:
    if i == 1:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0
print(max_count)

"""Time complexity : O(N)
    Space Complexity : O(1)"""

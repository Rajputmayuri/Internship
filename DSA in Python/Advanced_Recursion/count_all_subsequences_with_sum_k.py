from typing import List


def backtrack(index: int, total: int) -> int:
    # base cases
    if total == k:
        return 1
    if index >= len(nums) or total > k:
        return 0

    # include nums[index]
    pick = backtrack(index + 1, total + nums[index])
    # exclude nums[index]
    not_pick = backtrack(index + 1, total)

    return pick + not_pick


nums = [1, 2, 3, 4, 3, 2, 1, 1, 1, 1]
k = 3

count = backtrack(0, 0)
print(count)

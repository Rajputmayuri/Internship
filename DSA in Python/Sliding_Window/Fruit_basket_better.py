from typing import List


def findMaxFruits(arr: List[int], n: int) -> int:
    fruits = {}
    left = 0
    right = 0
    n = len(arr)
    max_length = 0

    while right < n:
        fruits[arr[right]] = fruits.get(arr[right], 0) + 1
        while len(fruits) > 2:
            fruits[arr[left]] -= 1
            if fruits[arr[left]] == 0:
                del fruits[arr[left]]
            left += 1
        max_length = max(max_length, right - left + 1)

        right += 1

    return max_length


print(findMaxFruits([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 2))

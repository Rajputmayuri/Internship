from typing import List


def findMaxFruits(arr: List[int], n: int) -> int:
    n = len(arr)
    max_length = 0
    for i in range(n):
        fruits = set()
        for j in range(i, n):
            fruits.add(arr[j])
            if len(fruits) > 2:
                break
            max_length = max(max_length, j - i + 1)

    return max_length


print(findMaxFruits([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 2))

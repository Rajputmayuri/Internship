from typing import List


class Solution:
    def backtrack(
        self,
        subset: List[int],
        index: int,
        target: int,
        result: set,
        candidates: List[int],
    ):
        if target == 0:
            result.add(tuple(subset.copy()))
        elif target < 0:
            return
        if index >= len(candidates):
            return
        subset.append(candidates[index])
        target -= candidates[index]
        self.backtrack(subset, index + 1, target, result, candidates)
        subset.pop()
        target += candidates[index]
        self.backtrack(subset, index + 1, target, result, candidates)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = set()
        self.backtrack([], 0, target, result, candidates)
        return list(result)


obj = Solution()
candidates = [1, 1, 2, 1, 2]
print(obj.combinationSum2(candidates, 4))

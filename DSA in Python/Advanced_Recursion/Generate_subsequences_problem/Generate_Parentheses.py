from typing import List


class Solution:
    def solve(self, index, total, brackets, result):
        if index >= len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return
        if total > len(brackets) // 2:
            return
        elif total < 0:
            return
        brackets[index] = "("
        sum = total + 1
        self.solve(index + 1, total + 1, brackets, result)
        brackets[index] = ")"
        sum = total - 1
        self.solve(index + 1, total - 1, brackets, result)

    def generateParanthesis(self, n) -> List[str]:
        brackets = [""] * (n * 2)
        result = []
        self.solve(0, 0, brackets, result)
        return result


obj = Solution()
print(obj.generateParanthesis(2))

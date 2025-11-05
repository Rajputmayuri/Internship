class Solution:
    def bitManipulation(self, num):
        num = num & (num - 1)
        return num


sol = Solution()
print(sol.bitManipulation(1))

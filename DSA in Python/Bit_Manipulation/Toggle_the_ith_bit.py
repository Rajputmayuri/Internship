class Solution:
    def bitManipulation(self, num, i):
        num = num ^ (1 << i)
        return num


sol = Solution()
print(sol.bitManipulation(15, 2))

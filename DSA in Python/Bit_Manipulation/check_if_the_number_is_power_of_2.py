class Solution:
    def bitManipulation(self, num):
        if num & (num - 1) == 0:
            return "power of 2"
        else:
            return "Not power of 2"


sol = Solution()
print(sol.bitManipulation(15))

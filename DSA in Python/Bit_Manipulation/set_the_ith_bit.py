class Solution:
    def bitManipulation(self, num, i):
        # convert to 0-based bit index
        i -= 1
        num = num | (1 << i)
        return num


sol = Solution()
print(sol.bitManipulation(70, 3))

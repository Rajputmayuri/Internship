class Solution:
    def bitManipulation(self, start, goal):
        ans = start ^ goal
        count = 0
        for i in range(0, 32):
            if ans & (1 << i) != 0:
                count += 1
        return count


sol = Solution()
print(sol.bitManipulation(10, 7))

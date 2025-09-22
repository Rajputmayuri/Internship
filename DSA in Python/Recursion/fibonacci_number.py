class Solution:
    def func(self, num):
        if num == 0 or num == 1:
            return num
        return self.func(num - 1) + (num - 2)


sol = Solution()
print(sol.func(10))

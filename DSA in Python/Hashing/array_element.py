"""
You're given an array (arr)
Return the frequency of element x in the given array
"""


class Solution:
    def findFrequency(self, arr, x):
        dic = {}
        for i in range(0, len(arr)):
            dic[arr[i]] = dic.get(arr[i], 0) + 1
        return dic.get(x, 0)


arr = [1, 2, 3, 1, 2, 3]
x = 2
sol = Solution()
print(sol.findFrequency(arr, x))

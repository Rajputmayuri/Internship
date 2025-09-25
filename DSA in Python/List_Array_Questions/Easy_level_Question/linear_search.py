class Solution:
    def search(self, arr, x):
        n = len(arr)
        for i in range(0, n):
            if arr[i] == x:
                return i
        return -1


sol = Solution()
arr = [1, 2, 3, 4, 5, 6]
print(sol.search(arr, 6))

"""Time Complexity : O(N)
   Space Complexity : O(1)"""

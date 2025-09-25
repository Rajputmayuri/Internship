class Solution:
    def isSorted(self, arr) -> bool:
        n = len(arr)
        for i in range(0, n - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True


sol = Solution()
print(sol.isSorted([4, 5, 7, 2, 1, 3]))

"""Time Complexity : O(N)
   Space Complexity : O(1)"""

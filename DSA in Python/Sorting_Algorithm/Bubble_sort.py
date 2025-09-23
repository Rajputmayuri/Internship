class Solution:
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n - 2, -1, -1):
            for j in range(0, i + 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


sol = Solution()
print(sol.bubbleSort([3, 5, 1, 6, 8, 9, 4]))

"""Time Complexity = o(N(N+1))/2 = o(N^2)
   Space complexity = o(1)"""

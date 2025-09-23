class Solution:
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


sol = Solution()
print(sol.selectionSort([8, 6, 4, 7, 2, 1, 3, 5]))

"""Time Complexity = o(N(N+1))/2 = o(N^2)
   Space complexity = o(1)"""

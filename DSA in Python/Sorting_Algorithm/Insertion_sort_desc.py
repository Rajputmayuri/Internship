class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


sol = Solution()
print(sol.insertionSort([7, 9, 8, 5, 4, 6, 1, 3, 2]))

"""Time Complexity = o(N(N+1))/2 = o(N^2)
   Space complexity = o(1)"""

"""1st Method"""


class Solution:
    def largest(self, arr):
        largest = arr[0]
        n = len(arr)
        for i in range(0, n):
            if arr[i] > largest:
                largest = arr[i]
        return largest


sol = Solution()
print(sol.largest([54, 95, 87, 63, 21, 85]))

"""2nd method"""


class Solution:
    def largest(self, arr):
        largest = arr[0]  # largest=float("-inf")
        n = len(arr)
        for i in range(0, n):
            largest = max(arr[i], largest)

        return largest


sol = Solution()
print(sol.largest([54, 95, 87, 63, 21, 85]))

"""Time Complexity : O(N)
    Space complexity : O(1)"""

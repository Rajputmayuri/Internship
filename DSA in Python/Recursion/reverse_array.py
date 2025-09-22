arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def func(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    func(arr, left + 1, right - 1)


func(arr, 0, 1)
print(arr)

"""------------------------------------"""


class Solution:
    def func(self, arr, left, right):
        if left >= right:
            return
        arr[left], arr[right] = arr[right], arr[left]
        self.func(arr, left + 1, right - 1)

    def reverseSubArray(self, arr, l, r):
        self.func(arr, l - 1, r - 1)
        return arr

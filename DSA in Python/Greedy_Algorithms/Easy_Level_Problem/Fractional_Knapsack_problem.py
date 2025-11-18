class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


class Solution:
    def fractionalknapsack(self, w, arr, n):
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        curWeight = 0
        finalvalue = 0.0
        for i in range(n):
            if curWeight + arr[i].weight <= w:
                curWeight += arr[i].weight
                finalvalue += arr[i].value
            else:
                remain = w - curWeight
                finalvalue += arr[i].value / arr[i].weight * remain
                break
        return finalvalue


arr = [Item(60, 10), Item(100, 20), Item(200, 50), Item(100, 50)]

sol = Solution()
n = len(arr)
print(sol.fractionalknapsack(90, arr, n))

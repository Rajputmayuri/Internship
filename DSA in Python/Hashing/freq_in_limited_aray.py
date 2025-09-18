class Solution:
    def frequencyCount(arr):
        n = len(arr)
        output = [0] * n

        for num in arr:
            if 1 <= num <= n:
                output[num - 1] += 1

        return output


arr = [2, 3, 3, 3, 6]
s = Solution.frequencyCount(arr)
print(s)

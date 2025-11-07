class Solution:
    def backtrack(self, subset, index, total):
        if total == K:
            return True
        if index >= N:
            return False

        subset.append(arr[index])
        pick = self.backtrack(subset, index + 1, total + arr[index])
        if pick == True:
            return True

        e = subset.pop()
        return self.backtrack(subset, index + 1, total)

    def checkSubsequenceSum(self, N, arr, K):
        return self.backtrack([], 0, 0)


# Example Input
N = 5
arr = [1, 2, 3, 4, 5]
K = 9

# Create object and call function
obj = Solution()
result = obj.checkSubsequenceSum(N, arr, K)

print(result)

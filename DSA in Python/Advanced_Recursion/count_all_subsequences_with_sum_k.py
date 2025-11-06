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

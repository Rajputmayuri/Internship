"""Brute Force Solution"""

arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
my_set = set()
for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for l in range(k + 1, n):
                if arr[i] + arr[j] + arr[k] + arr[l] == 0:
                    temp = [arr[i], arr[j], arr[k], arr[l]]
                    temp.sort()
                    my_set.add(tuple(temp))
print([list(ans) for ans in my_set])

# Time Complexity : O(N^3)
# Space Complexity : O(No. of triplets)

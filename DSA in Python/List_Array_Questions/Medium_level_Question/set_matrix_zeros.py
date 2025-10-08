"""Brute Force Solution"""


class Solution:
    def markInfinity(self, matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            if matrix[i][col] != 0:
                matrix[i][col] = float("inf")

        for j in range(c):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")

    def setZeroes(self, matrix):

        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    self.markInfinity(matrix, i, j)

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0


matrix = [[7, 10, 29, 3], [1, 20, 0, 4], [19, 0, 6, 11], [4, 27, 14, 7]]

Solution().setZeroes(matrix)
print(matrix)

"""Time Complexity : O((N+M)*(N*M))+O(N*M)
    Space Complexity :O(1"""

"""Optimal Solution"""
matrix = [[7, 10, 29, 3], [1, 20, 0, 4], [19, 0, 6, 11], [4, 27, 14, 7]]

r = len(matrix)
c = len(matrix[0])
rowtrack = [0 for _ in range(r)]
coltrack = [0 for _ in range(c)]
for i in range(0, r):
    for j in range(0, c):
        if matrix[i][j] == 0:
            rowtrack[i] = -1
            coltrack[j] = -1
for i in range(0, r):
    for j in range(0, c):
        if rowtrack[i] == -1 or coltrack[j] == -1:
            matrix[i][j] = 0
print(matrix)

"""Time Complexity : O(N*M)
    Space Compleixty : O(N+M)"""

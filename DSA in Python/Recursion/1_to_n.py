"""head recursion"""


def func(i, n):
    if i > n:
        return
    func(i + 1, n)  # head recursion
    print(i, end=" ")


func(1, 10)

"""2nd way"""


def func(i, n):
    if i > n:
        return
    print(i, end=" ")
    func(i + 1, n)  # tail recursion


func(1, 10)

"""using class"""


class Solution:
    def printNos(self, n):
        if n == 0:
            return
        self.printNos(n - 1)
        print(n, end=" ")


sol = Solution()
sol.printNos(10)

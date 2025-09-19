"""Print GFG without loop n times"""


def printGFG(n):
    if n == 0:
        return
    print("GFG", end=" ")
    printGFG(n - 1)


printGFG(10)

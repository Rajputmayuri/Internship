class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b


sol = Solution()
print(sol.get(15, 2))

###############################################################################

a = 5
b = 7

print("Before swap: a =", a, "b =", b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After swap:  a =", a, "b =", b)

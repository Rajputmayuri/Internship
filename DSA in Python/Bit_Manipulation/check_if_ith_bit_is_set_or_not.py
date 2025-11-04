"""using XOR << (left) shift operator"""


class Solution:
    def bitManipulation(self, num, i):
        if (num & (1 << i)) != 0:
            return True
        else:
            return False


sol = Solution()
print(sol.bitManipulation(13, 2))

##########################################################################3

"""using XOR >> (right) shift operator """


class Solution:
    def bitManipulation(self, num, i):
        if ((num >> i) & 1) == 1:
            return True
        else:
            return False


sol = Solution()
print(sol.bitManipulation(13, 1))

"""Time Complexity : O(1)"""
